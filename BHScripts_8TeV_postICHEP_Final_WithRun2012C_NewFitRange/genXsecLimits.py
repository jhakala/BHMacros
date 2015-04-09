import csv
from ModelParser import ModelParser, ModelGroup

models = []
with open("work/ModelXsecLimits.txt", "rb") as f:
   reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
   for row in reader:
      model = ModelParser(row)
      models.append(model)


from ROOT import TFile, TVectorD, TGraph
from Styles import formatXsecCL
from HistoStore import HistoStore
store = HistoStore()

group = ModelGroup(models)

for generator, group_generator in group.items():
   texfile = open("table_content-%s.tex" % generator, "w")
   for n, group_n in group_generator.items():
      for icolor, (MD, models) in enumerate(group_n.items()):
         vsize = len(models)
         vx = TVectorD(vsize)
         vxsec = TVectorD(vsize)
         vcl95 = TVectorD(vsize)
         vcla = TVectorD(vsize)

         for i,m in enumerate(models):
            vx[i] = m.M
            vxsec[i] = m.xsec
            vcl95[i] = m.cl95
            vcla[i] = m.cla

            bkg_str = ""
            if m.NbkgErr > m.Nbkg:
               bkg_str = "$%.2f ^{+%.2f}_{-%.2f}$" % (m.Nbkg, m.NbkgErr, m.Nbkg)
            else:
               bkg_str = "$%.2f \pm %.2f$" % (m.Nbkg, m.NbkgErr)

            texfile.write("%.1f & %.1f & %d & %.2f & %d & %.1f & %.1f & %.2f & %d & %s & %.3f & %.3f\\\\\n"\
                  % (m.MD, m.M, m.n, m.xsec, m.Nmin, m.STmin/1000.0, m.A*100.0, m.Nsig,\
                  m.Ndata, bkg_str, m.cl95, m.cla))

         #gxsec = TGraph(vx, vxsec)
         #gxsec.SetName("%s-MD%s_n%d-xsec" % (generator, MD, n))
         #formatXsecCL(gxsec, icolor)
         #store.book(gxsec)

         gcl95 = TGraph(vx, vcl95)
         gcl95.SetName("%s-MD%.1f_n%d-CL95" % (generator, MD, n))
         formatXsecCL(gcl95, icolor, 2)
         store.book(gcl95)

         gcla = TGraph(vx, vcla)
         gcla.SetName("%s-MD%.1f_n%d-CLA" % (generator, MD, n))
         formatXsecCL(gcla, icolor, 3)
         store.book(gcla)

         #spline
#         n_interpolation = 10
#         vx_spline = TVectorD((vsize-1) * n_interpolation)
#         vxsec_spline = TVectorD((vsize-1) * n_interpolation)
#         for i in range(vsize-1):
#            step = (vx[i+1] - vx[i]) / n_interpolation
#            for j in range(n_interpolation):
#               index = i*n_interpolation + j
#               vx_spline[index] = vx[i] + j*step
#               vxsec_spline[index] = gxsec.Eval(vx_spline[index], 0, "S")
#               
#         gxsec_spline = TGraph(vx_spline, vxsec_spline)
#         gxsec_spline.SetName("%s-MD%s_n%d-xsec-spline" % (generator, MD, n))
#         formatXsecCL(gxsec_spline, icolor)
#         store.book(gxsec_spline)

   texfile.close()

store.saveAs("work/XsecLimits.root")
