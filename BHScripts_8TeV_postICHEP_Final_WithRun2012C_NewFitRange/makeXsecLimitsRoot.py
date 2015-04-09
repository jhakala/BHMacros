#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-o", "--ouputfile", dest="outputfile")
   (options, args) = parser.parse_args()

   import configurations as config
   from ModelParser import ModelReader, ModelKey, GroupXsecLimit
   from OptimizationTools import Bisection
   from ROOT import TFile, TGraph

   groups = GroupXsecLimit(ModelReader(options.inputfile))
   group_mass_limits = dict()

   infile_xsec = TFile(config.bh_xsec, "READ")
   outfile = TFile(options.outputfile, "RECREATE")
   for key,group in groups.items():
      size = len(group)
      gCLA = TGraph(size)
      gCLA.SetName("%s-CLA" % key)
      gCL95 = TGraph(size)
      gCL95.SetName("%s-CL95" % key)

      for i,m in enumerate(group):
         gCLA.SetPoint(i, m.parameter["M"], m.cla)
         gCL95.SetPoint(i, m.parameter["M"], m.cl95)

      gCLA.Sort()
      gCLA.Write()
      gCL95.Write()
      gCL95.Write()

      gXsec = infile_xsec.Get(key)
      min_mass = Bisection(gCL95, gXsec)
      print min_mass

      print "%-30s%.2f" % (key,min_mass)

      if "BH" in key and min_mass < 14:
         model = ModelKey(key)
         key_mass_limit = "%s_%s-n%d" % (
               model.parameter["model"],
               model.parameter["generator"],
               model.parameter["n"])
         if key_mass_limit in group_mass_limits:
            group_mass_limits[key_mass_limit].append(\
                  (model.parameter["MD"], min_mass))
         else:
            group_mass_limits[key_mass_limit] = [\
                  (model.parameter["MD"], min_mass)]

   for key, limits in group_mass_limits.items():
      size = len(limits)
      gMassLimits = TGraph(size)
      gMassLimits.SetName(key)
      for i in range(size):
         gMassLimits.SetPoint(i, limits[i][0], limits[i][1])
      gMassLimits.Sort()
      gMassLimits.Write()

   outfile.Close()

if __name__ == "__main__":
   main()
