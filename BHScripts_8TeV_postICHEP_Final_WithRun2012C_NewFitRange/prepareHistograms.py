#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-o", "--ouputfile", dest="outputfile")
   (options, args) = parser.parse_args()

   from ROOT import TFile
   infile = TFile(options.inputfile, "READ")
   outfile = TFile(options.outputfile, "RECREATE")

   h = infile.Get("plots/ST")
   outfile.mkdir("plotsNoCut")
   outfile.cd("plotsNoCut")
   h.Write()

   h2D = infile.Get("plots/N_vs_ST")
   for N in [2,3]:
      i = h2D.GetYaxis().FindBin(N)
      h = h2D.ProjectionX("ST",i,i)
      outfile.mkdir("plotsN%d" % N)
      outfile.cd("plotsN%d" % N)
      h.Write()

   for N in range(2,11):
      i = h2D.GetYaxis().FindBin(N)
      h = h2D.ProjectionX("ST",i,-1)
      h.SetBinContent(900, 0)
      outfile.mkdir("plotsN%dup" % N)
      outfile.cd("plotsN%dup" % N)
      h.Write()

   h2D = infile.Get("plots/Njet_vs_ST")
   for N in [2,3]:
      i = h2D.GetYaxis().FindBin(N)
      h = h2D.ProjectionX("ST",i,i)
      outfile.mkdir("plots%dJets" % N)
      outfile.cd("plots%dJets" % N)
      h.Write()

   infile.Close()
   outfile.Close()

if __name__ == "__main__":
   main()
