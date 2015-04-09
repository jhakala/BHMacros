#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-o", "--ouputfile", dest="outputfile")
   parser.add_option("-l", "--logfile", dest="logfile")
   parser.add_option("-m", "--model", dest="model", type="string")
   (options, args) = parser.parse_args()

   model = options.model

   import csv
   import configurations as config
   from ROOT import TFile, gROOT, kFALSE
   from OptimizationTools import Integral, SignificanceHistogram
   gROOT.ProcessLine(".L roostats_cl95.C+")

   from ROOT import roostats_cl95, roostats_cla, roostats_limit


   ilum = config.integrated_luminosity
   slum = ilum * config.relative_luminosity_uncertainty
   seff = config.nominal_signal_uncertainty

   from BHXsec import BHXsec
   bhxsec =BHXsec()
   xsec = bhxsec.get(model)
   if xsec == -1:
      return

   sig_infile= TFile("%s/%s.root" % (config.bh_dir, model), "READ")
   if not sig_infile.IsOpen():
      return

   infile = TFile(options.inputfile, "READ")
   outfile = TFile(options.outputfile, "RECREATE")
   logfile = open(options.logfile, "w")

   outdir = outfile.mkdir(model)
   hST_NoCut = sig_infile.Get("plotsNoCut/ST")
   nEvents = hST_NoCut.GetEntries()
   Nmin = 0
   STmin = 0.0
   STmin_ibin = 0
   maxSignificance = 0.0
   for N in config.inclusive_multiplicities:
      hSig = sig_infile.Get("plotsN%dup/ST" % N)
      hSig.Rebin(config.rebin)
      hSig.Scale(xsec / nEvents * ilum)
      Integral(hSig)

      hBkg = infile.Get("IntegralBackground_N%dup" % N)

      result = SignificanceHistogram(hSig, hBkg)
      result.SetName("Significance_N%dup" % N)
      
      local_max = result.GetMaximum()
      if local_max > maxSignificance:
         maxSignificance = local_max
         Nmin = N
         STmin_ibin = result.GetMaximumBin()
         STmin = result.GetBinLowEdge(STmin_ibin)

      outdir.cd()
      result.Write()

   # Calculate xsec limits
   hData = infile.Get("IntegralData_N%dup" % Nmin)
   hBkg = infile.Get("IntegralBackground_N%dup" % Nmin)
   hSig = sig_infile.Get("plotsN%dup/ST" % Nmin)

   nData = int(hData.GetBinContent(STmin_ibin))
   nBkg = hBkg.GetBinContent(STmin_ibin)
   nBkgErr = hBkg.GetBinError(STmin_ibin)
   nSig = hSig.GetBinContent(STmin_ibin)
   eff = nSig/xsec/ilum
   seff *= eff
   
   print "Printing numbers "
   print ilum, slum, eff, seff, nBkg, nBkgErr, nData
   
   #CLs method
   rl = roostats_limit(ilum, slum, eff, seff, nBkg, nBkgErr, nData, kFALSE, 1, "cls", "my.png",12345)
   cl95 = rl.GetObservedLimit();
   cla =  rl.GetExpectedLimit();
   exp_up    = rl.GetOneSigmaHighRange();
   exp_down  = rl.GetOneSigmaLowRange();
   exp_2up   = rl.GetTwoSigmaHighRange(); 
   exp_2down = rl.GetTwoSigmaLowRange();  
    
   #WAS Bayesian a la:
   #cl95 = roostats_cl95(ilum, slum, eff, seff, nBkg, nBkgErr,
   #      nData, kFALSE, 1, "bayesian", "")
   #cla = roostats_cla(ilum, slum, 1.0, seff, nBkg, nBkgErr, 1)

   #logfile.write("%-25s %10.3e %d %d %8.3f %10.5e %8d %10.3e %10.3e %10.3e %10.3e\n"\
   #      % (model, xsec, Nmin, STmin, eff, nSig, nData, nBkg, nBkgErr, cl95, cla))

   logfile.write("%-25s %10.3e %d %d %8.3f %10.5e %8d %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e %10.3e\n"\
         % (model, xsec, Nmin, STmin, eff, nSig, nData, nBkg, nBkgErr, cl95, cla, exp_up, exp_down, exp_2up, exp_2down))

   sig_infile.Close()
   infile.Close()
   outfile.Close()
   logfile.close()

if __name__ == "__main__":
   main()
