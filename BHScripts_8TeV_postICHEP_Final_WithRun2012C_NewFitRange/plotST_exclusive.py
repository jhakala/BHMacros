#!/usr/bin/env python

def main():

   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-N", "--multiplicity", dest="N", type="int", default=3)
   parser.add_option("-x", "--exclusive", action="store_true",\
         dest="isExclusive", default=False)
   parser.add_option("-l", "--label", dest="label", type="string", default="")
   (options, args) = parser.parse_args()

   N = options.N
   isExclusive = options.isExclusive
   label_text = options.label

   if isExclusive and not (N == 2 or N == 3):
      parser.error("Exclusive plot only for N =2 or 3")

   import configurations as config
   from ROOT import TFile, TCanvas, THStack, TLegend, TPaveText, TH1F, gStyle, TGraph, TGraphErrors
   from ModelParser import ModelKey
   import array

   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)
   gStyle.SetOptStat(0000000)
   gStyle.SetOptFit(0000000)
   gStyle.SetErrorX(0.)
   suffix = ""
   if not isExclusive:
      suffix = "up"

   sm_files = []
   for model in config.sm_models:
      f = TFile("%s/%s.root" % (config.sm_dir, model), "READ")
      sm_files.append(f)

   bh_weights = []
   bh_files = []
   from BHXsec import BHXsec
   xsec = BHXsec()
   for model in config.bh_showcase:
      f = TFile("%s/%s.root" % (config.bh_dir, model), "READ")
      bh_files.append(f)
      h = f.Get("plotsNoCut/ST")
      nEvents= h.GetEntries()
      bh_weights.append(xsec.get(model) / nEvents * config.integrated_luminosity)

   c = TCanvas("ST_Mul%d%s" % (N, suffix),
         "ST_Mul%d%s" % (N, suffix), 500, 500)
   hs = THStack()
   hs1 = THStack()

   infile = TFile(options.inputfile, "READ")
   hBkg = infile.Get("Background_N%d%s" % (N, suffix))
   gBkg = infile.Get("BackgroundGraph_N%d%s" % (N, suffix))
   hData = infile.Get("Data_N%d%s" % (N, suffix))
   hBkg = infile.Get("Background_N%d%s" % (N, suffix))
   hBkg.SetMarkerSize(0)
   hBkg_ = hBkg.Clone("BkgLine")
   hBkg.SetFillColor(33)
   hBkg.SetLineColor(33)
   hBkg_.SetLineWidth(3)
   hBkg_.SetLineColor(862)
   hs.Add(hBkg, "e3")

   #n = 1
   #x = array.array('f', [100])
   #y = array.array('f', [100])
   #xx = array.array('f', [0])
   #yy = array.array('f', [100])
  
   #gr = TGraphErrors(1,x,y,xx,yy)
   #gr.SetMarkerStyle(20)
   #gr.Draw("pe")

   legend = TLegend(0.2826613,0.4819492,0.6094355,0.9416102) #was 0.4919492
   legend.SetTextSize(0.041); #was 0.02966102
   legend.SetTextFont(42);
   legend.SetFillColor(0)
   legend.SetLineColor(0)
   if isExclusive:
      legend.SetHeader("Multiplicity N = %d" % N)
   else:
      legend.SetHeader("Multiplicity N #geq %d" % N)
   legend.AddEntry(hData, "Data", "PEL")
   legend.AddEntry(hBkg_, "Background", "l")
   legend.AddEntry(hBkg, "Uncertainty", "f")

   legend_sm = TLegend(0.6271774,0.7369492,0.8308065,0.8771186)
   legend_sm.SetTextSize(0.041);
   legend_sm.SetTextFont(42);
   legend_sm.SetFillColor(0)
   legend_sm.SetLineColor(0)

   for i, f in enumerate(bh_files):
      h = f.Get("plotsN%d%s/ST" % (N, suffix))
      h.Rebin(config.rebin)
      h.Scale(bh_weights[i])

      # Add background
      for ibin in range(h.GetNbinsX()):
         h.SetBinContent(ibin+1,\
               h.GetBinContent(ibin+1)\
               + hBkg.GetBinContent(ibin+1))

         h.SetLineWidth(3)
         #h.SetLineColor(i+2)
         h.SetLineStyle(i+2)

         if i == 0:
            h.SetLineColor(814)
         if i == 1:
            h.SetLineStyle(5)
            h.SetLineColor(899)
         if i == 2:
            h.SetLineStyle(9)
            h.SetLineColor(4)
         if i == 3:
            h.SetLineStyle(3)
            h.SetLineColor(614)

      hs.Add(h, "hist")
      model = ModelKey(config.bh_showcase[i])
      bh_legend = "M_{D} = %.1f TeV, M_{BH}^{ min} = %.1f TeV, n = %d" % (\
            model.parameter["MD"],
            model.parameter["M"],
            model.parameter["n"])

      if i == 3:
         bh_legend = "M_{D} = 3.0 TeV, M_{QBH}^{ min} = 4.0 TeV, n = 4"    

      legend.AddEntry(h, bh_legend, "l")

   if isExclusive:
      for i, f in enumerate(sm_files):
         h = f.Get("plotsN%d%s/ST" % (N, suffix))
         h.Rebin(config.rebin)
         h.Scale(config.integrated_luminosity)
         h.SetFillColor(config.sm_colors[i])
         h.SetLineColor(config.sm_colors[i])
         hs1.Add(h, "hist")
         legend_sm.AddEntry(h, config.sm_models[i], "f")
   
   #hs.Add(hData, "e")  
    
   hs1.SetMinimum(1e-1)   
   hs1.Draw("")   
   hs.Draw("samenostack")  
   c.SetLogy(1)
   hs1.GetXaxis().SetTitle("S_{T} (GeV)")
   hs1.GetYaxis().SetTitle(hData.GetYaxis().GetTitle())
   hs1.GetYaxis().SetTitleOffset(1.25)

   hs1.GetYaxis().SetTitleSize(0.04)
   hs1.GetYaxis().SetLabelSize(0.04)
   hs1.GetXaxis().SetTitleSize(0.04)
   hs1.GetXaxis().SetLabelSize(0.04)
   hs1.GetXaxis().Draw() 
   ibin = 0
   #if isExclusive:
   #   hs1.GetXaxis().SetRangeUser(config.fit_range[0], 5550)
   #   ibin = hData.FindBin(config.fit_range[0])
   #else:
   #   hs1.GetXaxis().SetRangeUser(config.norm_range[0], config.norm_range[1])
   #   ibin = hData.FindBin(config.norm_range[0])

   if isExclusive:
      hs1.GetXaxis().SetRangeUser(1800, 5550)
      ibin = hData.FindBin(1800)
   else:
      hs1.GetXaxis().SetRangeUser(config.norm_range[0], config.norm_range[1])
      ibin = hData.FindBin(config.norm_range[0])

      
   from Styles import formatUncertainty
   formatUncertainty(gBkg)
   gBkg.Draw("LX")
   hData.GetXaxis().SetNdivisions(510)
   
   #hData.SetLineColor(1)
   hData.Draw("sameex0")

   hs1.SetMinimum(5e-1)
   if isExclusive:
      hs1.SetMaximum(1e7)#hData.GetBinContent(ibin) * 500)
   else:
      #hs.SetMaximum(4e4)
      hs1.SetMaximum(1e7)#hData.GetBinContent(ibin) * 500)

   legend.Draw("plain")
   if isExclusive:
      legend_sm.Draw("plain")

   if isExclusive:
      cmslabel =TPaveText(0.45,0.96,0.60,0.99,"brNDC");
   else:
      cmslabel = TPaveText(0.45,0.96,0.60,0.99,"brNDC")
   cmslabel.AddText(config.cmsTitle)
   #cmslabel.AddText(config.cmsSubtitle)
   cmslabel.SetFillColor(0)
   cmslabel.SetTextSize(0.041)
   cmslabel.Draw("plain")

   block1 =TPaveText(0.333,0.84,0.354,0.86,"brNDC");
   block1.SetFillColor(0)
   block1.Draw("plain")

   block2 =TPaveText(0.295,0.84,0.315,0.86,"brNDC");
   block2.SetFillColor(0)
   block2.Draw("plain")

   label = TPaveText(0.8891129,0.8644068,0.9435484,0.9258475,"brNDC")
   label.SetFillColor(0)
   label.SetTextSize(0.0529661);
   label.AddText(label_text);
   label.Draw("plain")
   
   if isExclusive:
     c.Print("ST_Mul%d.pdf" % N)
     c.Print("ST_Mul%d.png" % N)
   else:
     c.Print("ST_Mul%dup.pdf" % N)
     c.Print("ST_Mul%dup.png" % N)    
   c.Update()

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
