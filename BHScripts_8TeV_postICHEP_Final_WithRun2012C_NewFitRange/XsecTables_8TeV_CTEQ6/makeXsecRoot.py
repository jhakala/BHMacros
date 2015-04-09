#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("", "--spline3", action="store_true", dest="spline3", default=False)
   (options, args) = parser.parse_args()

   from ROOT import TFile, TGraph, TGraphErrors, NULL
   import csv

   with open(options.inputfile) as f:
      reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
      rows = list(reader)
      outfile = TFile("%s.root" % options.inputfile, "RECREATE")
      g = TGraphErrors(len(rows))

      for i, row in enumerate(rows):
         g.SetPoint(i, float(row[1])/1000., float(row[2]))
         g.SetPointError(i, 0.0, float(row[3]))

      if options.spline3:
         g_spline3 = TGraph(10*(g.GetN()-1))
         x = g.GetX()
         y = g.GetY()
         for i in range(g.GetN()-1):
            step = (x[i+1] - x[i]) / 10
            for j in range(10):
               index = 10*i + j;
               x_ = x[i] + j*step
               y_ = g.Eval(x_, NULL, "S")
               g_spline3.SetPoint(index, x_, y_)
         g_spline3.SetName(options.inputfile)
         g_spline3.Write()
      else:
         g.SetName(options.inputfile)
         g.Write()

      outfile.Close()

if __name__ == "__main__":
   main()
