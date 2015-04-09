#!/usr/bin/env python

def main():
   from optparse import OptionParser
   parser = OptionParser()
   parser.add_option("-i", "--inputfile", dest="inputfile")
   (options, args) = parser.parse_args()

   from ROOT import TFile, TCanvas, TPaveText, TLegend
   import configurations as config
   from Styles import formatCL

   infile = TFile(options.inputfile, "READ")
   oldfile = TFile(config.MI_old_file, "READ")
   store = []
   
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for iNmin, Nmin in enumerate(config.inclusive_multiplicities):
      c = TCanvas("UpperLimits_Inclusive_Mul%d" % Nmin,
           "N >= %d" % Nmin, 500, 500)
      store.append(c)
      gCL95 = infile.Get("CL95_N%dup" % Nmin)
      formatCL(gCL95, "CL95")
      gCL95.SetTitle("")
      gCL95.Draw("AL")

      gCLA = infile.Get("CLA_N%dup" % Nmin)
      formatCL(gCLA, "CLA")
      gCLA.SetTitle("")
      gCLA.Draw("L")

      label_11 = TPaveText(0.7116935,0.2076271,0.9193548,0.2605932,"brNDC")
      label_11.AddText(config.MI_new_label)
      label_11.SetTextSize(0.03813559);
      label_11.SetTextFont(42)
      label_11.SetFillColor(0)
      label_11.Draw("plain")
      store.append(label_11)

      if Nmin <= config.MI_old_Nmin:
         gCL95_ = oldfile.Get("CL95_N%dup" % Nmin)
         formatCL(gCL95_, "CL95", 2)
         gCL95_.SetLineStyle(9)
	 gCL95_.SetTitle("")
         gCL95_.Draw("L")

         gCLA_ = oldfile.Get("CLA_N%dup" % Nmin)
         formatCL(gCLA_, "CLA", 2)
	 gCLA_.SetTitle("")
         gCLA_.Draw("L")

         label_10 = TPaveText(0.6995968,0.4364407,0.9314516,0.4809322,"brNDC")
         label_10.AddText(config.MI_old_label)
         label_10.SetTextSize(0.03813559);
         label_10.SetTextFont(42)
         label_10.SetFillColor(0)
         label_10.Draw("plain")
         gCLA_.SetLineStyle(10)
         store.append(label_10)


      gCL95.GetXaxis().SetRangeUser(1100, config.MI_maxST + 100)
      gCL95.GetYaxis().SetRangeUser(3e-4, 20.0)
       
      cmslabel = TPaveText(0.3991935,0.7775424,0.8306452,0.9237288,"brNDC")
      cmslabel.AddText(config.cmsTitle)
      cmslabel.AddText(config.cmsSubtitle)
      cmslabel.SetFillColor(0)
      cmslabel.Draw("plain")
      store.append(cmslabel)

      legend = TLegend(0.5274194,0.5614407,0.8983871,0.7605932)
      legend.SetTextSize(0.04237288)
      legend.SetTextFont(42)
      legend.SetHeader("N #geq %d" % Nmin)
      legend.AddEntry(gCL95, "Observed #sigma^{95}", "l")
      legend.AddEntry(gCLA, "Expected #sigma^{95}_{exp.}", "l")
      legend.SetFillColor(0)
      legend.SetLineColor(0)
      legend.Draw("plain")
      store.append(legend)

      label = TPaveText(0.8891129,0.8644068,0.9435484,0.9258475,"brNDC")
      label.SetFillColor(0)
      label.SetTextSize(0.0529661);
      label.AddText("%s)" % alphabet[iNmin])
      label.Draw("plain")
      store.append(label)

      c.SetLogy(1)
      c.Print("UpperLimits_Inclusive_Mul%d.pdf" % Nmin)
      c.Update()

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
