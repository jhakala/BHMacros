class BHXsec:
   def __init__(self):
      import configurations as config
      from ROOT import TFile
      self.file = TFile(config.bh_xsec, "READ")

   def get(self, key):
      from ModelParser import ModelKey
      model = ModelKey(key)
      g = self.file.Get(model.getXsecLimitKey())
      if not g:
         return -1
      return g.Eval(model.parameter["M"])
