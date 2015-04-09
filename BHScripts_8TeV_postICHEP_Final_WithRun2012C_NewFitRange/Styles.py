pattle = [862, 814, 797, 899, 614, 921, 2, 4, 1]
marker = [20, 21, 22, 25, 24, 26]

from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle

gStyle.SetPadTopMargin(0.05)
gStyle.SetPadRightMargin(0.05)

def formatST(h):
   h.SetMarkerStyle(20)
   h.SetMarkerColor(923)
   h.SetLineColor(923)
   h.SetXTitle("S_{T} (GeV)")
   h.SetYTitle("Events / %d GeV" % h.GetBinWidth(1))
   h.GetYaxis().SetTitleOffset(1.1)
   h.GetYaxis().SetTitleSize(0.045)
   h.GetYaxis().SetLabelSize(0.045)
   h.GetXaxis().SetTitleSize(0.045)
   h.GetXaxis().SetLabelSize(0.045)
   
def formatTemplate(f, N, iformula):
   f.SetLineWidth(2)
   f.SetLineColor(pattle[iformula])
   if N == 2:
      f.SetLineStyle(1)
   elif N == 3:
      f.SetLineStyle(2)

def formatUncertainty(g):
   g.SetLineWidth(2)
   g.SetFillColor(862)
   #g.SetLineColor(33)
   g.SetLineColor(862)
   g.SetFillColor(33)
   #g.SetFillStyle()
   g.GetXaxis().SetTitle("S_{T} (GeV)")
   g.GetYaxis().SetTitle("Events / 100 GeV")
   g.GetYaxis().SetTitleOffset(1.1)
   g.GetYaxis().SetTitleSize(0.045)
   g.GetYaxis().SetLabelSize(0.045)
   g.GetXaxis().SetTitleSize(0.045)
   g.GetXaxis().SetLabelSize(0.045)
   
def formatCL(g, type, width=4):
   g.SetLineWidth(width)
   g.GetXaxis().SetTitle("S_{T}^{ min} (GeV)")
   g.GetXaxis().SetNdivisions(5,5,0)
   g.GetYaxis().SetTitle("#sigma(S_{T} > S_{T}^{ min}) #times A (pb)")
   g.GetYaxis().SetTitleOffset(1.045)
   g.GetYaxis().SetTitleSize(0.045)
   g.GetYaxis().SetLabelSize(0.045)
   g.GetXaxis().SetTitleSize(0.045)
   g.GetXaxis().SetLabelSize(0.045)
   
   if type == "CL95":
      g.SetLineColor(862)
      g.SetFillColor(862)
   elif type == "CLA":
      g.SetLineColor(899)
      g.SetFillColor(899)
      g.SetLineStyle(2)
   elif type == "CLA1":
      g.SetLineColor(899)
      g.SetFillColor(3)
      g.SetLineStyle(2)
      g.SetLineWidth(3)
   elif type == "CLA2":
      g.SetLineColor(899)
      g.SetFillColor(5)
      g.SetLineStyle(2)
      g.SetLineWidth(3)

def formatXsecCL(g, icolor, line_style=1):
   g.SetLineWidth(2)
   g.SetLineColor(pattle[icolor])
   g.SetLineStyle(line_style)
   g.SetMarkerColor(pattle[icolor])
   g.SetMarkerSize(1)
   g.GetXaxis().SetTitle("M_{BH}^{ min} (TeV)")
   g.GetYaxis().SetTitle("#sigma (pb)")
   g.GetYaxis().SetTitleOffset(1.2)

def formatExcludedMass(g, name = ""):
   g.GetXaxis().SetTitle("M_{D} (TeV)")
   g.GetYaxis().SetTitle("Excluded M_{BH}^{ min} (TeV)")
   g.GetYaxis().SetTitleOffset(1.1)
   g.GetYaxis().SetTitleSize(0.045)
   g.GetYaxis().SetLabelSize(0.045)
   
   if not name == "":
      g.SetLineWidth(3)
      g.SetMarkerSize(1)

   if "BH1_BM" in name or "BH4_CH" in name:
      color = 922
      marker_style = 20
      line_style = 1

   if "BH2_BM" in name or "BH2_CH" in name or "BH0_QB" in name:
      color = 862
      marker_style = 21
      line_style = 2

   if "BH8_CH" in name:
      color = 899
      marker_style = 22
      line_style = 3

   if "BH6_CH" in name or "BH5_BM" in name:
      color = 797
      marker_style = 20#34
      line_style = 1

   if "BH10_CH" in name:
      color = 2
      marker_style = 23
      line_style = 2
   
   if "BH9_CH" in name:
      color = 4
      marker_style = 24
      line_style = 3
         
   g.SetLineColor(color)
   g.SetLineStyle(line_style)
   g.SetMarkerStyle(marker_style)
   g.SetMarkerSize(1)
   g.SetMarkerColor(color)

def formatRatio(h, icolor):
   h.SetMarkerColor(pattle[icolor])
   #h.SetMarkerStyle(marker[icolor])
   h.SetLineColor(pattle[icolor])
