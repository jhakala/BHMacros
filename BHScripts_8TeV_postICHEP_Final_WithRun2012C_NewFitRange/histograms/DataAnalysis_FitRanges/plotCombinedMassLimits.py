#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   (options, args) = parser.parse_args()

   import configurations as config
   from Styles import formatExcludedMass

   from ROOT import gStyle
   from Styles import marker
   
   gStyle.SetPadTopMargin(0.05)
   gStyle.SetPadRightMargin(0.05)
   
   from ROOT import TFile, TCanvas, TMultiGraph, TLegend, TPaveText
   infile = TFile(options.inputfile, "READ")
   store = []


   for summary in config.summary_list:
      c = TCanvas(summary.name, summary.name, 500, 500)
      store.append(c)
      graphs = TMultiGraph()
      store.append(graphs)

      legend = TLegend(0.1394355,0.1694915,0.4955645,0.3733051)
      legend.SetHeader(summary.name)
      legend.SetTextSize(0.02966102);
      legend.SetFillColor(0)
      legend.SetLineColor(0)
      store.append(legend)

      addLegend = True
      for n in summary.n:
         for model in summary.models:
            key = "%s_%s-n%d" % (model, summary.generator,n)
            g = infile.Get(key)
            formatExcludedMass(g, key)
            graphs.Add(g, "pl")

            if addLegend:
               legend_key = "%s_%s" % (model, summary.generator)
               legend.AddEntry(g, config.model_description[legend_key], "pl")

         addLegend = False

      graphs.Draw("a")
      graphs.GetXaxis().SetTitle("M_{D} (TeV)")
      graphs.GetYaxis().SetTitle("Excluded M_{BH}^{ min} (TeV)")
      graphs.GetYaxis().SetTitleOffset(1.2)

      legend.Draw("plain")

      cmslabel = TPaveText(0.5201613,0.7775424,0.9416129,0.9237288,"brNDC")
      cmslabel.AddText(config.cmsTitle)
      cmslabel.AddText(config.cmsSubtitle)
      cmslabel.SetFillColor(0)
      cmslabel.Draw("plain")
      store.append(cmslabel)

      label_n2 = TPaveText(0.8245968,0.25,0.9254032,0.3029661,"brNDC")
      label_n2.AddText("n = 2")
      label_n2.SetTextFont(42)
      label_n2.SetFillColor(0)
      label_n2.Draw("plain")
      store.append(label_n2)

      label_n4 = TPaveText(0.8407258,0.5042373,0.9415323,0.5572034,"brNDC")
      label_n4.AddText("n = 4")
      label_n4.SetTextFont(42)
      label_n4.SetFillColor(0)
      label_n4.Draw("plain")
      store.append(label_n4)

      label_n6 = TPaveText(0.8387097,0.6419492,0.9395161,0.6949153,"brNDC")
      label_n6.AddText("n = 6")
      label_n6.SetTextFont(42)
      label_n6.SetFillColor(0)
      label_n6.Draw("plain")
      store.append(label_n6)

      c.Update()

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
