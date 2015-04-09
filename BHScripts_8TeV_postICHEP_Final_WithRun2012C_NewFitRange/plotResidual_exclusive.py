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
   from ROOT import TFile, TCanvas, THStack, TLegend, TPaveText, TH1F, gStyle
   from ModelParser import ModelKey

   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)
   gStyle.SetOptStat(0000000)

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
   
   hData_N2 = infile.Get("Data_N2")
   hBkg_N2 = infile.Get("Background_N2")

   ratio_data = infile.Get("Data_N%d%s" % (N, suffix))
   ratio_data.Sumw2()
   ratio_data.Divide(hData_N2,hBkg_N2)

   ref_N2 = infile.Get("ReferenceTemplateN2_0")
   ref_N3 = infile.Get("ReferenceTemplateN3_0")
   ratio_fits = infile.Get("ReferenceTemplateN2_0")
   ratio_fits.Sumw2()
   ratio_fits.Divide(ref_N2,ref_N3)
 
   legend = TLegend(0.3026613,0.6919492,0.6094355,0.8816102)
   legend.SetTextSize(0.041); #was 0.02966102
   legend.SetTextFont(42);
   legend.SetFillColor(0)
   legend.SetLineColor(0)
   if isExclusive:
      legend.SetHeader("Multiplicity, N = %d" % N)
   else:
      legend.SetHeader("Multiplicity, N #geq %d" % N)
   legend.AddEntry(ratio_data, "Data/Background", "p")
   legend.AddEntry(ratio_fits, "Fit-0 (N=2)/Fit-0 (N=3)", "l")

   legend_sm = TLegend(0.6271774,0.6769492,0.8308065,0.8171186)
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

         h.SetLineWidth(2)
         h.SetLineStyle(i+2)

      hs.Add(h, "hist")
      model = ModelKey(config.bh_showcase[i])
      bh_legend = "M_{D} = %.1f TeV, M_{BH}^{ min} = %.1f TeV, n = %d" % (\
            model.parameter["MD"],
            model.parameter["M"],
            model.parameter["n"])

      #legend.AddEntry(h, bh_legend, "l")

   if isExclusive:
      for i, f in enumerate(sm_files):
         h = f.Get("plotsN%d%s/ST" % (N, suffix))
         h.Rebin(config.rebin)
         h.Scale(config.integrated_luminosity)
         h.SetFillColor(config.sm_colors[i])
         h.SetLineColor(config.sm_colors[i])
         hs1.Add(h, "hist")
         #legend_sm.AddEntry(h, config.sm_models[i], "f")
   
   #hs.Add(hData, "e")  
   #TH1F *ratio_data 
    
   ratio_fits.SetLineColor(4)
   ratio_fits.SetMarkerStyle(0)
   ratio_fits.SetLineWidth(2)
   
   #hs1.SetMinimum(1e-1)   
   ratio_fits.Draw("linee1")
   ratio_data.Draw("same")   
   #hs.Draw("samenostack")  
   #c.SetLogy(1)
   ratio_fits.GetXaxis().SetTitle("S_{T} (GeV)")
   ratio_fits.GetYaxis().SetTitle("Arbitrary Units")
   ratio_fits.GetYaxis().SetTitleOffset(1.1)

   ratio_fits.GetYaxis().SetTitleSize(0.045)
   ratio_fits.GetYaxis().SetLabelSize(0.045)
   ratio_fits.GetXaxis().SetTitleSize(0.045)
   ratio_fits.GetXaxis().SetLabelSize(0.045)
   ratio_fits.GetXaxis().Draw() 
   ibin = 0
   if isExclusive:
      ratio_fits.GetXaxis().SetRangeUser(config.fit_range[0], config.fit_range[1]+330)
      ibin = hData.FindBin(config.fit_range[0])
   else:
      ratio_fits.GetXaxis().SetRangeUser(config.norm_range[0], config.norm_range[1]+330)
      ibin = hData.FindBin(config.norm_range[0])
   from Styles import formatUncertainty
   formatUncertainty(gBkg)
   #gBkg.Draw("LX")
   #hData.GetXaxis().SetNdivisions(510)
   
   #hData.Draw("esame")
   ratio_fits.SetTitle("")
   ratio_fits.SetMinimum(0)
   ratio_fits.SetMaximum(3)
   
   legend.Draw("plain")
   #if isExclusive:
   #   legend_sm.Draw("plain")

   if isExclusive:
      cmslabel =TPaveText(0.45,0.90,0.60,0.93,"brNDC");
   else:
      cmslabel = TPaveText(0.45,0.90,0.60,0.93,"brNDC")
   cmslabel.AddText(config.cmsTitle)
   #cmslabel.AddText(config.cmsSubtitle)
   cmslabel.SetFillColor(0)
   cmslabel.SetTextSize(0.041)
   cmslabel.Draw("plain")

   label = TPaveText(0.8891129,0.8644068,0.9435484,0.9258475,"brNDC")
   label.SetFillColor(0)
   label.SetTextSize(0.0529661);
   label.AddText(label_text);
   label.Draw("plain")
   
   if isExclusive:
     c.Print("ST_Residuals_Mul%d.pdf" % N)
     c.Print("ST_Residuals_Mul%d.png" % N)
   else:
     c.Print("ST_Mul%dup.pdf" % N)
     c.Print("ST_Mul%dup.png" % N)    
   c.Update()

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
