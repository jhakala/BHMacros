#!/usr/bin/env python

def main():
   import configurations as config
   import csv
   from ModelParser import ModelKey, GroupXsecLimit
   from ROOT import gStyle
   from Styles import marker
   
   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)

   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   (options, args) = parser.parse_args()

   models = []
   with open(config.bh_list, 'rb') as f:
      reader = csv.reader(f)
      for r in reader:
         models.append(ModelKey(r[0]))

   from ROOT import TFile, TMultiGraph, TGraph, TLegend, TCanvas
   infile_xsec = TFile(config.bh_xsec, "READ")
   infile_CL = TFile(options.inputfile, "READ")

   from OptimizationTools import Bisection
   from Styles import formatXsecCL, formatExcludedMass

   store = []
   mg = TMultiGraph()
   legend1 = TLegend(0.3241611,0.49,0.746644,0.69)
   legend1.SetHeader("Observed Cross Section Limits")
   legend1.SetTextSize(0.037)
   legend1.SetTextFont(42)
   legend1.SetFillColor(0)
   legend1.SetLineColor(0)

   legend2 = TLegend(0.3241611,0.68,0.746644,0.88)
   legend2.SetHeader("Theoretical Cross Section")
   legend2.SetTextSize(0.037)
   legend2.SetTextFont(42)
   legend2.SetFillColor(0)
   legend2.SetLineColor(0)
   
   legend3 = TLegend(0.3241611,0.8806993,0.886644,0.9273427)
   legend3.SetHeader("String Ball (BlackMax)")
   legend3.SetTextSize(0.037)
   legend3.SetTextFont(42)
   legend3.SetFillColor(0)
   legend3.SetLineColor(0)
   
   iColor = 0
   iStyle = 2
   #for key, group in ModelLimitGroup(models).items():
   for key, group in GroupXsecLimit(models).items():
      if not "SB" in key:
         continue
         
      name = ModelKey(key).name
      gXsec = infile_xsec.Get(key)
      formatXsecCL(gXsec, iColor, iStyle)
      mg.Add(gXsec, "c")
      legend2.AddEntry(gXsec, config.model_description[name], "l")

      gCL95 = infile_CL.Get("%s-CL95" % key)
      formatXsecCL(gCL95, iColor, 1)
      mg.Add(gCL95, "pl")
      legend1.AddEntry(gCL95, config.model_description[name], "pl")

      iColor += 1
      iStyle += 2

   c = TCanvas("SB_BM", "SB_BM", 500, 500)
   c.SetLogy()
   mg.Draw("A")
   mg.GetXaxis().SetTitle("M^{ min} (TeV)")
   mg.GetXaxis().SetRangeUser(3.9,7.1)
   mg.GetYaxis().SetRangeUser(1e-4,50)
   mg.GetYaxis().SetTitle("#sigma (pb)")
   mg.GetYaxis().SetTitleOffset(1.05)
   mg.GetYaxis().SetTitleSize(0.045)
   mg.GetYaxis().SetLabelSize(0.045)
   mg.GetXaxis().SetTitleSize(0.045)
   mg.GetXaxis().SetLabelSize(0.045)
   
   legend1.Draw("plain")
   legend2.Draw("plain")
   legend3.Draw("plain")
   c.Update()

   from ROOT import TPaveText
   cmslabel = TPaveText(0.45,0.96,0.60,0.99,"brNDC")
   cmslabel.AddText(config.cmsTitle)
   cmslabel.SetTextSize(0.041)
   #cmslabel.AddText(config.cmsSubtitle)
   cmslabel.SetFillColor(0)
   cmslabel.Draw("plain")

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
