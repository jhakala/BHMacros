import configurations as config
from ROOT import TH1D, TMath, TF1

def Integral(histo):
   for i in range(histo.GetNbinsX(), 0, -1):
      histo.SetBinContent(i, histo.GetBinContent(i) + histo.GetBinContent(i+1))
      histo.SetBinError(i, histo.GetBinError(i) + histo.GetBinError(i+1))

def LogLikelihood(histo, template, scale, minST, maxST):
   result = 0.0

   firstbin = histo.FindBin(minST)
   lastbin = histo.FindBin(maxST)
   for i in range(firstbin, lastbin):
      n = histo.GetBinContent(i)
      f = scale * template.GetBinContent(i)
      #f = scale * template.Eval(histo.GetBinCenter(i))
      log_f = TMath.Log(f)
      result += n * log_f - f
   return result

def OptimizeScale(histo, template, norm_range):
   minST = norm_range[0]
   maxST = norm_range[1]

   # First Scan
   ibin1 = histo.FindBin(minST)
   ibin2 = histo.FindBin(maxST)
   est_scale = histo.Integral(ibin1, ibin2)
   est_scale /= template.Integral(ibin1, ibin2)
   est_error = 0.2 * est_scale

   histo_lnL = TH1D("lnL_scan", "lnL_scan", 100,
         est_scale - est_error, est_scale + est_error)
   max_lnL = -9.e999;
   for i in range(1,101):
      trial = histo_lnL.GetBinCenter(i)
      lnL = LogLikelihood(histo, template, trial, minST, maxST)
      histo_lnL.SetBinContent(i, lnL)
      if lnL > max_lnL:
         max_lnL = lnL
         est_scale = trial

   min_delta = 1e999
   for i in range(1,101):
      trial = histo_lnL.GetBinCenter(i)
      delta = histo_lnL.GetBinContent(i) - max_lnL + 0.5
      if abs(delta) < min_delta:
         min_delta = abs(delta)
         est_error = abs(est_scale - trial)
   #print est_scale, est_error

   # Second scan and fit
   histo_lnL = TH1D("lnL", "lnL", 100,
         est_scale - 1.2*est_error,
         est_scale + 1.2*est_error)
   for i in range(1,101):
      trial = histo_lnL.GetBinCenter(i)
      lnL = LogLikelihood(histo, template, trial, minST, maxST)
      histo_lnL.SetBinContent(i, lnL - max_lnL)

   fit_lnL  = TF1('fit_lnL', 'pol2')
   histo_lnL.Fit(fit_lnL, 'Q0')
   est_scale = -fit_lnL.GetParameter(1) / 2.0 / fit_lnL.GetParameter(2)
   est_error = 1.0 / TMath.Sqrt(-2.0 * fit_lnL.GetParameter(2))

   #print est_scale, est_error
   return histo_lnL, est_scale, est_error

def SignificanceHistogram(hSignal, hBkg):
   h = hSignal.Clone("Significance")
   h.Reset()
   lastbin = h.FindBin(config.com)
   for i in range(1, lastbin):
      nBkg = hBkg.GetBinContent(i)
      nSignal = hSignal.GetBinContent(i)
      nBkg_err = hBkg.GetBinError(i)

      nTotal = nBkg + nSignal
      
      print nBkg, nSignal, nBkg_err, nTotal
	    
      significance = 0.0
      if nTotal > 0:
         significance = nSignal / TMath.Sqrt(nTotal)
         h.SetBinContent(i, significance)

   return h

def Bisection(g1=0, g2=0):
   start = 3.0
   end = 14.0
   
   x1 = g1.GetX()
   max_x1 = x1[g1.GetN()-1]
   x2 = g2.GetX()
   max_x2 = x2[g2.GetN()-1]

   lo = start
   hi = end
   if g1.Eval(start) - g2.Eval(start) > 0:
      lo = end
      hi = start

   mid = lo + (hi - lo)/2.0
   while mid != lo and mid != hi:
      if mid > max_x1:
         value1 = g1.Eval(max_x1)
      else:
         value1 = g1.Eval(mid)

      if mid > max_x2:
         value2 = g2.Eval(max_x2)
      else:
         value2 = g2.Eval(mid)

      #value1 = g1.Eval(mid)
      #value2 = g2.Eval(mid)

      if value1 - value2 <= 0:
         lo = mid
      else:
         hi = mid
      mid = lo + (hi - lo)/2.0
   return mid
