#!/usr/bin/env python

def main():

   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-N", "--multiplicity", dest="N", type="int", default=3)
   parser.add_option("-x", "--exclusive", action="store_true",\
         dest="isExclusive", default=False)
   parser.add_option("-l", "--label", dest="label", type="string", default="")
   parser.add_option("-z", "--zeyneplabel",action="store_true",dest="zeynep",default=True)
   (options, args) = parser.parse_args()

   N = options.N
   isExclusive = options.isExclusive
   label_text = options.label

   zeynep = options.zeynep

   if isExclusive and not (N == 2 or N == 3):
      parser.error("Exclusive plot only for N =2 or 3")

   import configurations as config
   from ROOT import TFile, TCanvas, THStack, TLegend, TPaveText, gStyle, TPad, TH1F, TGraphAsymmErrors, TMath
   from ModelParser import ModelKey

   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)
   gStyle.SetPadBottomMargin(0.20)

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
         "ST_Mul%d%s" % (N, suffix), 500, 600)
   hs = THStack()
   hs1 = THStack()

   infile = TFile(options.inputfile, "READ")
   hBkg = infile.Get("Background_N%d%s" % (N, suffix))
   #hnewBkg = infile.Get("histoTemplateN3_0")
   hnewBkg = infile.Get("ReferenceTemplateN3_0")
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
   hnewBkg.SetLineWidth(3)
   hnewBkg.Scale(10*3.407)
   hs.Add(hnewBkg,"l")


   
   legend = TLegend(0.2826613,0.4819492,0.6094355,0.9416102) # - only for N >= 2 and 3
   #legend = TLegend(0.3026613,0.5519492,0.6094355,0.9416102) # was 0.4919...zeynep
   
   #legend = TLegend(0.3526613,0.5519492,0.6094355,0.9416102) # was 0.4919...

   #legend.SetTextSize(0.041); #was 0.02966102
   legend.SetTextSize(0.037);
   legend.SetTextFont(42);
   legend.SetFillColor(0)
   legend.SetLineColor(0)
   if isExclusive:
      legend.SetHeader("Multiplicity N = %d" % N)
   else:
      legend.SetHeader("Multiplicity N #geq %d" % N)
   legend.AddEntry(hData, "Data", "lep")
   #legend.AddEntry(hnewBkg, "N=3 Fit Rescaled","l")
   legend.AddEntry(hBkg_, "Background", "l")
   legend.AddEntry(hBkg, "Uncertainty", "f")

   legend_sm = TLegend(0.6471774,0.7069492,0.8508065,0.8471186)
#   legend_sm = TLegend(0.6271774,0.7369492,0.8308065,0.8771186)
#   legend_sm.SetTextSize(0.037);
   legend_sm.SetTextSize(0.037);

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
         
         #if i == 0:
            #h.SetLineColor(814)
         if i == 0:
            h.SetLineStyle(5)
            h.SetLineColor(899)
         if i == 1:
            h.SetLineStyle(9)
            h.SetLineColor(4)
         if i == 2:
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

#      qbh_legend = "M_{D} = 4.0 TeV, M_{QBH}^{ min} = 5.0 TeV, n = 5"

#      legend.AddEntry(h, qbh_legend, "l")
  
   #if isExclusive:
   zeynep = True
   if zeynep:
      for i, f in enumerate(sm_files):
         h = f.Get("plotsN%d%s/ST" % (N, suffix))
         h.Rebin(config.rebin)
         h.Scale(config.integrated_luminosity)
         h.SetFillColor(config.sm_colors[i])
         h.SetLineColor(config.sm_colors[i])
         hs1.Add(h, "hist")
         legend_sm.AddEntry(h, config.sm_models[i], "f")
   
   #hs.Add(hData, "e")   

   
   hs.Draw("nostack")
   hs1.Draw("same")

   c.SetLogy(1)
   hs.GetXaxis().SetTitle("S_{T} (GeV)")
   hs.GetYaxis().SetTitle(hData.GetYaxis().GetTitle())
   hs.GetYaxis().SetTitleOffset(1.25)

   hs.GetYaxis().SetTitleSize(0.04)
   hs.GetYaxis().SetLabelSize(0.04)
   hs.GetXaxis().SetTitleSize(0.01)
   hs.GetXaxis().SetLabelSize(0.01)
    
   ibin = 0
   #if isExclusive:
   #   hs.GetXaxis().SetRangeUser(config.fit_range[0], config.maxST)
   #   ibin = hData.FindBin(config.fit_range[0])
   #else:
   #   hs.GetXaxis().SetRangeUser(config.norm_range[0], config.maxST)
   #   ibin = hData.FindBin(config.norm_range[0])
   
   if isExclusive:
      hs.GetXaxis().SetRangeUser(1800, config.maxST)
      ibin = hData.FindBin(1800)
   else:
      hs.GetXaxis().SetRangeUser(config.norm_range[0], config.maxST)
      ibin = hData.FindBin(config.norm_range[0])

   from Styles import formatUncertainty
   formatUncertainty(gBkg)
   gBkg.Draw("LX")
   hData.Draw("sameex0")

   hs.SetMinimum(5e-1)
   if isExclusive:
      hs.SetMaximum(1e7)
 #     hs.SetMaximum(hData.GetBinContent(ibin) * 40)
   else:
      #hs.SetMaximum(1e8)
      hs.SetMaximum(hData.GetBinContent(ibin) * 20) # or 1e7 for N>=3 and use 4 models

   legend.Draw("plain")
   #if isExclusive:
   if zeynep:
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

   label = TPaveText(0.8891129,0.8644068,0.9435484,0.9258475,"brNDC")
   label.SetFillColor(0)
   #label.SetTextSize(0.0529661);
   label.SetTextSize(0.0529661);
   label.AddText(label_text);
   label.Draw("plain")

   c.RedrawAxis()


      #Divide
   
   ibin = hData.FindBin(config.norm_range[0])
   #print ibin

   fbin = hData.FindBin(config.maxST)
   #print fbin

   hData.Sumw2()
   hBkg_.Sumw2()

   Pull = TH1F("","",fbin-ibin+1,(ibin-1)*100,fbin*100)
   Pull2 = TH1F("","",fbin-ibin+1,(ibin-1)*100,fbin*100)

   Ratio = hData.Clone()
   Ratio.Add(hBkg_,-1)
   #Ratio.Divide(hBkg_) 

   Band = TGraphAsymmErrors(fbin-ibin+1)
   
   for i in range(ibin-1,fbin+1):
      i += 1
      if hData.GetBinContent(i) != 0:
         value = hData.GetBinContent(i) + (hBkg_.GetBinError(i)*hBkg_.GetBinError(i))
         #print Ratio.GetBinError(i),  value**(0.5)
         #print i-19,i,(i)*100, hData.GetBinContent(i) , hBkg_.GetBinContent(i),hData.GetBinContent(i) - hBkg_.GetBinContent(i)
         Pull.SetBinContent(i-19,(hData.GetBinContent(i) - hBkg_.GetBinContent(i))/ Ratio.GetBinError(i))
         #print Ratio.GetBinError(i), abs(Ratio.GetBinContent(i))*0.05
         #Pull.SetBinContent(i-19,(hData.GetBinContent(i) - hBkg_.GetBinContent(i))/ Ratio.GetBinError(i))
         #Pull.SetBinContent(i-19,(hData.GetBinContent(i) / hBkg_.GetBinContent(i)))
         Pull.SetBinError(i-19,Ratio.GetBinError(i))
         #Pull.SetBinError(i-19,hData.GetBinError(i)/gBkg.GetErrorY(i))
         if (hBkg_.GetBinContent(i)*0.05 >  hBkg_.GetBinError(i)):
            #print "bin error too small changing the error to: ", hBkg_.GetBinContent(i)*0.05
            Pull2.SetBinContent(i-19,(hnewBkg.GetBinContent(i) - hBkg_.GetBinContent(i))/ (hBkg_.GetBinContent(i)*0.05))
         else:
            Pull2.SetBinContent(i-19,(hnewBkg.GetBinContent(i) - hBkg_.GetBinContent(i))/ hBkg_.GetBinError(i))
         #print hBkg_.GetBinError(i), hBkg_.GetBinContent(i)*0.05
         #print i, " Pull2: ", Pull2.GetBinContent(i-19), "hnewBkg.GetBinContent(i-1): " , hnewBkg.GetBinContent(i-1), "hBkg_.GetBinContent(i): ", hBkg_.GetBinContent(i)
      else:
         Pull.SetBinContent(i-19,0)
         Pull2.SetBinContent(i-19,(hnewBkg.GetBinContent(i-1) - hBkg_.GetBinContent(i))/ hBkg_.GetBinError(i))

                  
      Band.SetPoint(i,hBkg_.GetBinCenter(i),1.0)
      #print hBkg_.GetBinContent(i), hBkg_.GetBinError(i)
      up   = abs ( 1.- ((hBkg_.GetBinContent(i) + hBkg_.GetBinError(i)) / hBkg_.GetBinContent(i)))
      down = abs ( 1.- ((hBkg_.GetBinContent(i) - hBkg_.GetBinError(i)) / hBkg_.GetBinContent(i)))
      Band.SetPointError(i,0.,0.,down,up)

      
 
   #Band.Print()
   pad = TPad("pad", "pad", 0.0, 0.0, 1.0, 1.0)

   pad.SetTopMargin(0.799999)
   pad.SetRightMargin(0.05)
   pad.SetBottomMargin(0.09)

   pad.SetFillColor(0)
   #pad.SetGridy(1)
   pad.SetFillStyle(0)
   pad.Draw("same")
   pad.cd(0)

   Ratio.SetMarkerStyle(20)
   Pull.SetMarkerStyle(20)
   Pull.SetLineColor(1)
   Pull.SetMarkerSize(0.9)
   #Pull.SetMaximum(3)
   #Pull.SetMinimum(-1)

   Pull.SetMaximum(2.5)
   Pull.SetMinimum(-2.5)
   Pull.GetYaxis().SetNdivisions(5,1);

   Pull.GetXaxis().SetTitle('S_{T} (GeV)')
   Pull.GetXaxis().SetLabelSize(0.04)
   
   Pull.GetYaxis().SetTitleOffset(1.05)
   Pull.GetYaxis().SetLabelSize(0.02)
   Pull.GetYaxis().SetTitleSize(0.025)
   Pull.GetYaxis().CenterTitle(1)


   Pull.GetYaxis().SetTitle('#sigma(Data-Bkg)')

   Pull.SetFillColor(2)
   Pull.Draw("HIST")
   Pull2.SetLineColor(862)
   Pull2.SetLineWidth(3)
   Pull2.SetLineStyle(2)
   #Pull2.Draw("SAME")
   formatUncertainty(Band)
   Band.SetFillStyle(3001)
   
  # Band.Draw("le3")
  # Pull.Draw("ex0same")
   pad.RedrawAxis()

   gStyle.SetOptStat(0)
   

   #block1 =TPaveText(0.370,0.84,0.351,0.86,"brNDC"); # for N>=2 and >=3 only
   #block1 =TPaveText(0.361,0.85,0.377,0.87,"brNDC");
   #block1 =TPaveText(0.333,0.88,0.354,0.85,"brNDC") #for n = 2 only


   block1 =TPaveText(0.331,0.82,0.357,0.85,"brNDC"); #FOR n=3 only
   block1.SetFillColor(0)
   block1.Draw("plain")

   #block2 =TPaveText(0.305,0.84,0.333,0.86,"brNDC"); # for N>=2 and >=3 only
   #block2 =TPaveText(0.395,0.85,0.41,0.87,"brNDC");
   #block2 =TPaveText(0.296,0.88,0.316,0.85,"brNDC"); for n =2 only

   block2 =TPaveText(0.295,0.82,0.317,0.85,"brNDC");  #FOR n=3 only
   block2.SetFillColor(0)
   block2.Draw("plain")
   
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
