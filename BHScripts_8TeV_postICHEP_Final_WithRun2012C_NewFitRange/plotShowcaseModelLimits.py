#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   (options, args) = parser.parse_args()

   from ROOT import TFile, TCanvas, TPaveText, TLegend, TMultiGraph
   import configurations as config
   from Styles import pattle, marker
   from ModelParser import ModelKey
   from ROOT import gStyle
   
   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)

   infile_xsec = TFile(config.bh_xsec, "READ")
   infile_CL = TFile(options.inputfile, "READ")

   c = TCanvas("MassLimits","MassLimits",500,500)
   mg = TMultiGraph()

   legend1 = TLegend(0.4541611,0.510839,0.836644,0.6597203)
   legend1.SetHeader("Observed Cross Section Limits")
   legend1.SetTextSize(0.037)
   legend1.SetTextFont(42)
   legend1.SetFillColor(0)
   legend1.SetLineColor(0)

   legend2 = TLegend(0.4541611,0.6806993,0.836644,0.8173427)
   legend2.SetHeader("Theoretical Cross Section")
   legend2.SetTextSize(0.037)
   legend2.SetTextFont(42)
   legend2.SetFillColor(0)
   legend2.SetLineColor(0)
   
   legend3 = TLegend(0.4541611,0.8206993,0.836644,0.8673427)
   legend3.SetHeader("Nonrotating Black Holes")
   legend3.SetTextSize(0.037)
   legend3.SetTextFont(42)
   legend3.SetFillColor(0)
   legend3.SetLineColor(0)
   
   for i,m in enumerate(config.limit_showcase):
      model = ModelKey(m)
      gxsec = infile_xsec.Get(m)
      gxsec.SetLineWidth(2)
      gxsec.SetLineStyle(2)
      gxsec.SetLineColor(pattle[i])
      mg.Add(gxsec, "l")

      legend2.AddEntry(gxsec, "M_{D} = %.1f TeV, n = %d"
            % (model.parameter["MD"], model.parameter["n"]), "l")

      gcl95 = infile_CL.Get("%s-CL95" % m)
      gcl95.SetLineWidth(2)
      gcl95.SetLineStyle(1)
      gcl95.SetLineColor(pattle[i])
      gcl95.SetMarkerColor(pattle[i])
      gcl95.SetMarkerSize(1)
      gcl95.SetMarkerStyle(marker[i])
      mg.Add(gcl95, "pl")
      legend1.AddEntry(gcl95, "M_{D} = %.1f TeV, n = %d"
            % (model.parameter["MD"], model.parameter["n"]), "pl")

   mg.Draw("a")
   mg.SetMinimum(5e-4)
   mg.SetMaximum(9e1)
   mg.GetXaxis().SetRangeUser(3.6,7.6)
   mg.GetXaxis().SetTitle("M_{BH}^{ min} (TeV)")
   mg.GetYaxis().SetTitle("#sigma (pb)")
   mg.GetYaxis().SetTitleOffset(1.05)
   mg.GetYaxis().SetTitleSize(0.04)
   mg.GetYaxis().SetLabelSize(0.04)
   mg.GetXaxis().SetTitleSize(0.04)
   mg.GetXaxis().SetLabelSize(0.04)
   
   c.SetLogy(1)
   cmslabel = TPaveText(0.45,0.90,0.60,0.93,"brNDC")
   cmslabel.AddText(config.cmsTitle)
   cmslabel.SetTextSize(0.041)
   #cmslabel.AddText(config.cmsSubtitle)
   cmslabel.SetFillColor(0)
   cmslabel.Draw("plain")
   legend1.Draw("plain")
   legend2.Draw("plain")
   legend3.Draw("plain")
   c.Update()
   c.Print("MassLimits.pdf")
   c.Print("MassLimits.png")

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
