def main():
   from ROOT import TFile
   import configurations as config

   infile = TFile("Templates.root", "READ")
   infileCL = TFile("MI.root", "READ")


   for Nmin in config.inclusive_multiplicities:

      texfile = open("latex/tableModelIndependentLimits_N%d.tex" % Nmin, "w")
      #texfile.write("\\begin{table}\n")
      #texfile.write("\\centering\n")
      #texfile.write("\\begin{tabular}{*{6}r}\n")
      #texfile.write("\\hline\n")
      #texfile.write("$N^\\mathrm{min}$ & $S_T^{\\mathrm{min}}$ (TeV)")
      #texfile.write("& $n^\mathrm{data}$ & $n^\\mathrm{bkg}$ &")
      #texfile.write("$\\sigma^{95}$ (pb)& $\\sigma^{95}_\\mathrm{exp.}$ (pb)\\\\")
      #texfile.write("\\hline\n")

      hData = infile.Get("IntegralData_N%dup" % Nmin)
      hBkg = infile.Get("IntegralBackground_N%dup" % Nmin)

      gCL95 = infileCL.Get("CL95_N%dup" % Nmin)
      gCLA = infileCL.Get("CLA_N%dup" % Nmin)

      firstbin = hData.FindBin(1000)
      lastbin = hData.FindBin(config.MI_maxST)

      for i in range(firstbin, lastbin):
         STmin = hData.GetBinLowEdge(i)
         nData = hData.GetBinContent(i)
         nBkg = hBkg.GetBinContent(i)
         nBkgErr = hBkg.GetBinError(i)
         cl95 = gCL95.Eval(STmin)
         cla = gCLA.Eval(STmin)

         if nBkgErr > nBkg:
            texfile.write("%d & %.1f & %d & $%.2f ^{+%.2f}_{-%.2f}$ & %.4f & %.4f \\\\\n"\
                  % (Nmin, STmin/1000., nData, nBkg, nBkgErr, nBkg, cl95, cla))

         else:
            texfile.write("%d & %.1f & %d & $%.2f \pm %.2f$ & %.4f & %.4f \\\\\n"\
                  % (Nmin, STmin/1000.0, nData, nBkg, nBkgErr, cl95, cla))

      #texfile.write("\\hline\n")
      #texfile.write("\\end{tabular}\n")
      #texfile.write("\\end{table}")
      texfile.close()

if __name__ == "__main__":
   main()
