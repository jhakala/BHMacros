#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   parser.add_option("-o", "--ouputfile", dest="outputfile")
   parser.add_option("-b", "--batch", action="store_true",\
         dest="isBatch", default=False)
   parser.add_option("--normalization", nargs=2,\
         type="float", dest="norm_range")
   parser.add_option("--fit", nargs=2,\
         type="float", dest="fit_range")
   (options, args) = parser.parse_args()

   isSaveOutput = options.outputfile is not None

   if not (options.inputfile):
      parser.error("Please specify inputfiles.")

   import configurations as config
   if options.fit_range:
      fit_range = options.fit_range
      norm_range = (fit_range[1] - 200., fit_range[1])
   else:
      fit_range = config.fit_range
      norm_range = config.norm_range

   # Override normalization range from input
   if options.norm_range:
      norm_range = options.norm_range


   from Styles import formatST, formatTemplate, formatUncertainty
   from ROOT import TFile, TF1, TH1D, TMath, TCanvas, TLegend,\
         TGraphAsymmErrors, TVectorD

   #input file name
   infile = TFile(options.inputfile, "READ")

   from HistoStore import HistoStore
   store = HistoStore()
   canvas = HistoStore()

   print "Fit range: %d - %d GeV" % fit_range
   print "Normalization range: %d - %d GeV" % norm_range

   # Fit
   for N in config.exclusive_multiplicities:
      hST = infile.Get("plots%dJets/ST" %  N)
      if not options.isBatch:
         c = TCanvas("TemplateN%d" % N, 
               "TemplateN%d" % N, 500, 500)
         canvas.book(c)
         formatST(hST)
         hST.Draw("e")
         hST.GetXaxis().SetRangeUser(fit_range[0], config.maxST)
         hST.GetYaxis().SetRangeUser(1e-2, 2e4)
         c.SetLogy(1)

      for i,formula in enumerate(config.templates):
         if N == 2:
            f = TF1("templateN%d_%d" % (N, i), formula, 0, 10000)
         elif N == 3:
            f = store.get("templateN2_%d" % i).Clone("templateN%d_%d" % (N, i))
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         hST.Fit(f, "QN0", "", fit_range[0], fit_range[1])
         if i == 0:
            hST.Fit(f, "Q0", "", fit_range[0], fit_range[1])

         formatTemplate(f, N, i)
         store.book(f)

         if not options.isBatch:
            f.Draw("same")

         hTemplate = hST.Clone("histoTemplateN%d_%d" % (N,i))
         hTemplate.Reset()
         hTemplate.Eval(f)
         formatTemplate(hTemplate, N, i)
         store.book(hTemplate)

         if i == 0:
            hRef = hTemplate.Clone("ReferenceTemplateN%d_0" % N)
            store.book(hRef)

         # Print Chi-squre/Ndof
         print "N = %d, Chi^2/Ndof = %0.2f/%d" %\
               (N, f.GetChisquare(), f.GetNDF())
      if not options.isBatch:
         c.Update()

   # Calculate scale/error
   from OptimizationTools import OptimizeScale
   for histoN, templateN in [[2,3]]:
      hST = store.get("ReferenceTemplateN%d_0" % histoN)
      hTemplate  = store.get("ReferenceTemplateN%d_0" % templateN)

      hlnL, scale, err = OptimizeScale(hST, hTemplate, norm_range)
      hlnL.SetName("LogLikelihood_%dto%d" % (templateN, histoN))
      store.book(hlnL)

      for i in range(len(config.templates)):
         hTemplate  = store.get("histoTemplateN%d_%d" % (templateN, i))
         hTemplate_ = hTemplate.Clone("histoTemplateN%d_%d__RescaledToN%d"
               % (templateN, i, histoN))
         hTemplate_.Scale(scale)
         store.book(hTemplate_)

   # Shape Uncertainty
   hBkgTemplate  = store.get("histoTemplateN2_0")
   hBkgTemplate.Rebin(config.rebin)
   nbins = hBkgTemplate.GetNbinsX()
   vST = TVectorD(nbins)
   vBkg = TVectorD(nbins)
   vexl = TVectorD(nbins)
   vexh = TVectorD(nbins)
   shape_el = TVectorD(nbins)
   shape_eh = TVectorD(nbins)
   rel_shape_el = TVectorD(nbins)
   rel_shape_eh = TVectorD(nbins)
   for i in range(nbins):
      vST[i] = hBkgTemplate.GetBinCenter(i+1)
      if (vST[i] < config.com):
         vBkg[i] = hBkgTemplate.GetBinContent(i+1)
      else:
         vBkg[i] = 0.0
      vexl[i] = 0.0
      vexh[i] = 0.0
      shape_el[i] = 0.0
      shape_eh[i] = 0.0
      rel_shape_el[i] = 0.0
      rel_shape_eh[i] = 0.0

   for i in range(len(config.templates)):
      for label in ["histoTemplateN2_%d", "histoTemplateN3_%d__RescaledToN2"]:
         if label % i == "histoTemplateN2_0":
            continue
         h = store.get(label % i)
         h.Rebin(config.rebin)
         for ibin in range(nbins):
            diff = h.GetBinContent(ibin+1) - vBkg[ibin]
            if diff > 0 and diff > shape_eh[ibin]:
               shape_eh[ibin] = diff
            elif diff < 0 and abs(diff) > shape_el[ibin]:
               shape_el[ibin] = abs(diff)

   # Relative Shape Uncertaincy
   for i in range(nbins):
      if vBkg[i] > 0:
         #rel_shape_el[i] = rel_shape_el[i] / vBkg[i]
         #hape_eh[i] = rel_shape_eh[i] / vBkg[i]
         max_err = max(shape_el[i], shape_eh[i])
         shape_el[i] = max_err
         shape_eh[i] = max_err
         rel_shape_el[i] = max_err /vBkg[i]
         rel_shape_eh[i] = max_err /vBkg[i]
      else:
         rel_shape_el[i] = 0.0
         rel_shape_eh[i] = 0.0
      #print vST[i], vBkg[i], rel_shape_el[i], rel_shape_eh[i]
   gShapeUncertainty = TGraphAsymmErrors(vST, vBkg,
         vexl, vexh, shape_el, shape_eh)
   gShapeUncertainty.SetName("Shape_Uncertainty")
   formatUncertainty(gShapeUncertainty)
   store.book(gShapeUncertainty)

   gRelShapeUncertainty = TGraphAsymmErrors(vST, vexl,
         vexl, vexh, rel_shape_el, rel_shape_eh)
   gRelShapeUncertainty.SetName("Relative_Shape_Uncertainty")
   formatUncertainty(gRelShapeUncertainty)
   store.book(gRelShapeUncertainty)

   # Generate Backgrouds
   for N in config.label_for_data:
      hST = infile.Get("plotsN%s/ST" % N)
      rel_scale_err2 = 0.0
      scale_factor = 1.0
      for Nref in config.label_for_ref:
         if N == Nref:
            continue

         template = store.get("ReferenceTemplateN%s_0" % Nref)

         hlnL, scale, err = OptimizeScale(hST, template, norm_range)
         hlnL.SetName("LogLikelihood_%sto%s" % (Nref, N))
         store.book(hlnL)

         if Nref == "2":
            scale_factor = scale
         rel_scale_err2 += err/scale * err/scale

         print "%s/%s %.3f +/- %.3f" % (N, Nref, scale, err)

      vy = TVectorD(nbins)
      veyh = TVectorD(nbins)
      veyl = TVectorD(nbins)
      for i in range(nbins):
         vy[i] = vBkg[i] * scale_factor
         veyh[i] = vy[i] * TMath.Sqrt(rel_scale_err2 
               + rel_shape_eh[i]*rel_shape_eh[i])
         veyl[i] = vy[i] * TMath.Sqrt(rel_scale_err2 
               + rel_shape_el[i]*rel_shape_el[i])

      print "Scaling uncertainty (%s): %.2f" %\
            (N, TMath.sqrt(rel_scale_err2) * 100.0)

      gBkg = TGraphAsymmErrors(vST, vy, vexl, vexh, veyl, veyh)
      gBkg.SetName("BackgroundGraph_N%s" % N)
      formatUncertainty(gBkg)
      store.book(gBkg)

      hST.Rebin(config.rebin)
      hST.SetName("Data_N%s" % N)
      formatST(hST)
      store.book(hST)

      hBkg = hST.Clone("Background_N%s" % N)
      hBkg.Reset()
      store.book(hBkg)

      for i in range(nbins):
         ibin = hBkg.FindBin(vST[i])
         hBkg.SetBinContent(ibin, vy[i])
         hBkg.SetBinError(ibin, max(veyh[i], vexl[i]))

      from OptimizationTools import Integral
      hIntBkg = hBkg.Clone("IntegralBackground_N%s" % N)
      Integral(hIntBkg)
      store.book(hIntBkg)

      hIntData = hST.Clone("IntegralData_N%s" % N)
      Integral(hIntData)
      store.book(hIntData)

   # Plot Shape Uncertainty
   if not options.isBatch:
      legend_shape = TLegend(0.5544355,0.5741525,0.9495968,0.9152542)
      legend_shape.SetTextFont(42)
      legend_shape.SetFillColor(0)
      c = TCanvas("ShapeUncertaintyN2", "ShapeUncertaintyN2", 500, 500)
      canvas.book(c)
      gShapeUncertainty.Draw("AC3")
      gShapeUncertainty.GetXaxis().SetRangeUser(fit_range[0], config.maxST)
      gShapeUncertainty.GetYaxis().SetRangeUser(5e-2, 1.2e6)
      legend_shape.AddEntry(store.get("Data_N2"), "Data (N = 2)", "p")
      legend_shape.AddEntry(gShapeUncertainty, "Shape Uncertainty", "f")
      for i in range(len(config.templates)):
         for label in ["histoTemplateN2_%d", "histoTemplateN3_%d__RescaledToN2"]:
            h = store.get(label % i)
            h.GetXaxis().SetRangeUser(fit_range[0], config.maxST)
            h.Draw("histcsame")
            if label == "histoTemplateN2_%d":
               N = 2
            else:
               N = 3
            legend_shape.AddEntry(h, "Parametrization %d (N = %d)" % (i, N), "l")
      store.get("Data_N2").Draw("esame")
      c.SetLogy(1)
      legend_shape.Draw("plain")
      c.Update()

   if isSaveOutput:
      store.saveAs(options.outputfile)

   if not options.isBatch:
      raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
