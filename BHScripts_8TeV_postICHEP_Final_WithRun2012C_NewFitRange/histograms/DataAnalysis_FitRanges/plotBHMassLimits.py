#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-m", "--model", dest="model", type="string")
   (options, args) = parser.parse_args()

   from ROOT import TFile, TMultiGraph, TCanvas, TLegend
   from Styles import formatXsecCL
   import configurations as config
   from ROOT import gStyle

   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)

   infile = TFile(options.inputfile, "READ")
   infile_xsec = TFile(config.bh_xsec, "READ")

   store = []
   for n in config.extraDim_list:
      c = TCanvas("%s-n%d" % (options.model,n),\
            "%s-n%d" % (options.model,n),\
            500, 500)
      store.append(c)

      graphs = TMultiGraph()
      store.append(graphs)

      legend = TLegend(0.5266129,0.5360169,0.9476613,0.9364407)
      legend.SetTextSize(0.02966102);
      legend.SetFillColor(0)
      legend.SetLineColor(0)
      legend.SetHeader("n = %d" % n)
      store.append(legend)

      for i,MD in enumerate(config.MD_list):
         gCL95 = infile.Get("%s-MD%.1f_n%d-CL95" % (options.model, MD, n))
         gXsec = infile_xsec.Get("%s-MD%.1f_n%d" % (options.model, MD, n))

         if gCL95 and gXsec:
            legend.AddEntry(gCL95, "M_{D} = %.1f TeV Observed" % MD, "l")
            formatXsecCL(gCL95, i, 1)
            graphs.Add(gCL95, "l")

            legend.AddEntry(gXsec, "M_{D} = %.1f TeV Theoretical" % MD, "l")
            formatXsecCL(gXsec, i, 2)
            graphs.Add(gXsec, "c")

      graphs.Draw("a")
      graphs.GetXaxis().SetTitle("M_{BH}^{ min} (TeV)")
      graphs.GetYaxis().SetTitle("#sigma (pb)")
      graphs.GetYaxis().SetTitleOffset(1.2)
      graphs.GetXaxis().SetRangeUser(3.5,6.5)
      graphs.SetMinimum(1e-3)
      graphs.SetMaximum(1e2)
      c.SetLogy()
      legend.Draw("plain")
      c.Print("MassLimit_%s_n%d.pdf" % (options.model,n))
      c.Update()

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
