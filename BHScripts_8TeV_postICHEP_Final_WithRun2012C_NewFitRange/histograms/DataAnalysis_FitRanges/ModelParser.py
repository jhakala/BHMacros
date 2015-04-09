def ModelReader(infilename, readCSV=True):
   import csv
   models = []
   with open(infilename, "rb") as f:
      reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
      for row in reader:
         model = ModelKey(row[0])
         if readCSV:
            model.readCSV(row)
         models.append(model)
   return models

#def GetSummaryKeys(models):
#   keys = {}
#   for model in models:
#      if "SB" in model.name:
#         continue
#      generator = model.parameter["generator"]
#      key = "%s-n%d" % (model.name, model.parameter["n"])
#      if generator in keys:
#         keys[generator].add(key)
#      else:
#         keys[generator] = set([key])
#   return keys

class ModelKey:
   def __init__(self, key):
      self.parameter = dict()
      self.key=key 
      tokens = key.split("-")
      self.name = tokens[0]
      tokens1 = tokens[0].split("_")
      self.parameter["model"] = tokens1[0]
      self.parameter["generator"] = tokens1[1]
      tokens2 = tokens[1].split("_")
      keys = ["MD", "M", "n", "Ms", "gs"]
      for token in tokens2:
         for key in keys:
            try:
               self.parameter[key] = float(token.replace(key,""))
               break
            except ValueError:
               continue

   def __repr__(self):
      return self.key

   def __lt__(self, other):
      if "BH" in self.name:
         keys = ["generator", "model", "MD", "n", "M"]
      elif "SB" in self.name:
         keys = ["generator", "model", "Ms", "gs", "MD", "M"]
      for key in keys:
         if key not in self.parameter:
            continue
         if self.parameter[key] < other.parameter[key]:
            return True
         elif self.parameter[key] > other.parameter[key]:
            return False
      return False

   def getXsecLimitKey(self):
      return self.key.replace("M%.1f_" % self.parameter["M"], "")

   def readCSV(self, row):
      self.xsec = float(row[1])
      self.Nmin = int(row[2])
      self.STmin = float(row[3])
      self.A = float(row[4])
      self.Nsig = float(row[5])
      self.Ndata = int(row[6])
      self.Nbkg = float(row[7])
      self.NbkgErr = float(row[8])
      self.cl95 = float(row[9])
      self.cla = float(row[10])

   def texRow(self):
      bkg_str = ""
      if self.NbkgErr > self.Nbkg:
         bkg_str = "$%.2f ^{+%.2f}_{-%.2f}$" % (self.Nbkg, self.NbkgErr, self.Nbkg)
      else:
         bkg_str = "$%.2f \pm %.2f$" % (self.Nbkg, self.NbkgErr)

      if "BH" in self.parameter["model"]:
         return "%.1f & %.1f & %d\
               & %.3g & %d & %.1f & %.1f & %.2f\
               & %d & %s & %.3f & %.3f\\\\"\
               % (self.parameter["MD"], self.parameter["M"], self.parameter["n"],\
               self.xsec, self.Nmin, self.STmin/1000.0, self.A*100.0, self.Nsig, \
               self.Ndata, bkg_str, self.cl95, self.cla)
      else:
         return "%.1f & %.1f & %.1f & %.1f\
               & %.2g & %d & %.1f & %.1f & %.2f & %d & %s & %.3f & %.3f\\\\"\
               % (self.parameter["MD"], self.parameter["M"],\
               self.parameter["Ms"], self.parameter["gs"],\
               self.xsec, self.Nmin, self.STmin/1000.0, self.A*100.0, self.Nsig,\
               self.Ndata, bkg_str, self.cl95, self.cla)

# group models as a function of min. BH mass
def GroupXsecLimit(models):
   group = dict()
   for model in models:
      key = model.getXsecLimitKey()
      if key in group:
         group[key].append(model)
      else:
         group[key] = [model]
   return group 

def ModelLimitGroup(models):
   models.sort()
   group = dict()
   prev_group_key = ""
   for model in models:
      if model.getGroupKey() == prev_group_key:
         continue
      prev_group_key = model.getGroupKey()

      if "BH" in model.name:
         key = "%s-n%d" % (model.name, model.parameter["n"])
      elif "SB" in model.name:
         key = "%s-Ms%.1f_gs%.1f" % (model.name,\
               model.parameter["Ms"], model.parameter["gs"])
      if key in group:
         group[key].append(model)
      else:
         group[key] = [model]
   return group
