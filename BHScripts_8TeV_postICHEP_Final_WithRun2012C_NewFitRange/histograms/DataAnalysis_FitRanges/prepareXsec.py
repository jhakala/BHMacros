from ModelParser import XsecParser, ModelGroup
import csv

from ROOT import TGraphErrors, TVectorD
from HistoStore import HistoStore

store = HistoStore()
models = []
with open("xsec_tmp2.txt", "rb") as f:
   reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
   for row in reader:
      model =XsecParser(row)
      models.append(model)

group = ModelGroup(models)

for generator, group_generator in group.items():
   for n, group_n in group_generator.items():
      for icolor, (MD, models) in enumerate(group_n.items()):
         vsize = len(models)
         vx = TVectorD(vsize)
         vxsec = TVectorD(vsize)
         vex = TVectorD(vsize)
         vey = TVectorD(vsize)

         for i,m in enumerate(models):
            vx[i] = m.M
            vex[i] = 0.0
            vxsec[i] = m.xsec
            vey[i] = m.xsecErr

         g =TGraphErrors(vx, vxsec, vex, vey)
         g.SetName("%s-MD%.1f_n%d-xsec" % (generator, MD, n))
         store.book(g)

store.saveAs("xsec_tmp2.root")
