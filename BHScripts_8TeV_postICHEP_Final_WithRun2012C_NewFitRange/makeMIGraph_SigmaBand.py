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
      gCLA1sup = TGraph(len(rows))
      gCLA1sup.SetName("CLA1sup_N%dup" % options.N)
      gCLA2sup = TGraph(len(rows))
      gCLA2sup.SetName("CLA2sup_N%dup" % options.N)
      gCLA1sdn = TGraph(len(rows))
      gCLA1sdn.SetName("CLA1sdn_N%dup" % options.N)
      gCLA2sdn = TGraph(len(rows))
      gCLA2sdn.SetName("CLA2sdn_N%dup" % options.N)
      gCLA1s = TGraph(2*len(rows))
      gCLA1s.SetName("CLA1s_N%dup" % options.N)
      gCLA2s = TGraph(2*len(rows))
      gCLA2s.SetName("CLA2s_N%dup" % options.N)
      
      print len(rows)
      for i, row in enumerate(rows):
         #print i, row
         gCL95.SetPoint(i, float(row[0]), float(row[1]))
         gCLA.SetPoint(i, float(row[0]), float(row[2]))
         gCLA1sup.SetPoint(i, float(row[0]), float(row[3]))
         gCLA1sdn.SetPoint(i, float(row[0]), float(row[4]))
         gCLA2sup.SetPoint(i, float(row[0]), float(row[5]))
         gCLA2sdn.SetPoint(i, float(row[0]), float(row[6]))
         gCLA1s.SetPoint(i, float(row[0]), float(row[3]))
         gCLA2s.SetPoint(i, float(row[0]), float(row[5]))

      for j, row in enumerate(rows):
         #print j
         gCLA1s.SetPoint(2*len(rows)-j-1, float(row[0]), float(row[4]))
         gCLA2s.SetPoint(2*len(rows)-j-1, float(row[0]), float(row[6]))

      gCL95.Write()
      gCLA.Write()
      gCLA1sup.Write()
      gCLA1sdn.Write()
      gCLA2sup.Write()
      gCLA2sdn.Write()
      gCLA1s.Write()
      gCLA2s.Write()

      outfile.Close()

if __name__ == "__main__":
   main()
