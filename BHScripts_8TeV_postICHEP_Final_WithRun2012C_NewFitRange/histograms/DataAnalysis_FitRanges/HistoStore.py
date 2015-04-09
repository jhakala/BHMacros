class HistoStore:
   def __init__(self):
      self.store = {}

   def book(self, h):
      self.store[h.GetName()] = h

   def get(self, name):
      return self.store[name]

   def find(self, name):
      if name in self.store:
         return self.store[name]
      else:
         return None

   def saveAs(self, filename):
      from ROOT import TFile
      outfile = TFile(filename, "RECREATE")
      for name, h in self.store.items():
         h.Write()
      outfile.Close()
