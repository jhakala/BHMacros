#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-o", "--outputfile", dest="outputfile")
   parser.add_option("-N", "--multiplicity", dest="N", type="int")
   (options, args) = parser.parse_args()

   from ROOT import TFile, TGraph
   import csv

   with open(options.inputfile) as f:
      reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
      rows = list(reader)
      outfile = TFile(options.outputfile, "RECREATE")
      gCL95 = TGraph(len(rows))
      gCL95.SetName("CL95_N%dup" % options.N)
      gCLA = TGraph(len(rows))
      gCLA.SetName("CLA_N%dup" % options.N)

      for i, row in enumerate(rows):
         gCL95.SetPoint(i, float(row[0]), float(row[1]))
         gCLA.SetPoint(i, float(row[0]), float(row[2]))
      gCL95.Write()
      gCLA.Write()
      outfile.Close()

if __name__ == "__main__":
   main()
