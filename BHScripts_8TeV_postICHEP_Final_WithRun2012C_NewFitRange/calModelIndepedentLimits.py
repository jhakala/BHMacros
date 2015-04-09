#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-l", "--logfile", dest="logfile")
   parser.add_option("-N", "--multiplicity", dest="N", type="int")
   parser.add_option("", "--ST", dest="ST", type="int")
   (options, args) = parser.parse_args()

   from ROOT import gROOT, TFile, kFALSE, TGraph, TVectorD
   gROOT.ProcessLine(".L roostats_cl95.C+")

   from ROOT import roostats_cl95, roostats_cla, roostats_limit
   import configurations as config
   ilum = config.integrated_luminosity
   slum = ilum * config.relative_luminosity_uncertainty
   seff = config.nominal_signal_uncertainty

   infile = TFile(options.inputfile, "READ")

   from HistoStore import HistoStore
   store = HistoStore()

   hIntBkg = infile.Get("IntegralBackground_N%dup" % options.N)
   hIntData = infile.Get("IntegralData_N%dup" % options.N)

   ibin = hIntData.FindBin(options.ST)
   nBkg = hIntBkg.GetBinContent(ibin)
   sBkg = hIntBkg.GetBinError(ibin)
   nData = int(hIntData.GetBinContent(ibin))

   print "%10d %10.2f +/- %10.2f" % (nData, nBkg, sBkg)
   print ilum, slum, 1.0, seff,  nBkg, sBkg, nData
   #CLs method
   rl = roostats_limit(ilum, slum, 1.0, seff, nBkg, sBkg, nData, kFALSE, 1, "cls", "my.png",23576)
   cl95 = rl.GetObservedLimit();
   cla =  rl.GetExpectedLimit();
   exp_up    = rl.GetOneSigmaHighRange();
   exp_down  = rl.GetOneSigmaLowRange();
   exp_2up   = rl.GetTwoSigmaHighRange(); 
   exp_2down = rl.GetTwoSigmaLowRange();  
    
   #WAS Bayesian a la:
   #cl95 = roostats_cl95(ilum, slum, 1.0, seff, nBkg, sBkg, nData, kFALSE, 1, "bayesian", "")
   #cla = roostats_cla(ilum, slum, 1.0, seff, nBkg, sBkg, 1)
   
   logfile = open(options.logfile, "w")
   logfile.write("%-10d %-10.5f %-10.5f %-10.5f %-10.5f %-10.5f %-10.5f\n" % (options.ST, cl95, cla, exp_up, exp_down, exp_2up, exp_2down))
   logfile.close()

if __name__ == "__main__":
   main()
