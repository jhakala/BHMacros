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
      
      gCLA2s = infile.Get("CLA2s_N%dup" % Nmin)
      formatCL(gCLA2s, "CLA2")
      gCLA2s.SetTitle("")
      gCLA2s.SetFillColor(5)
      gCLA2s.Draw("ALF")  
        
      gCLA1s = infile.Get("CLA1s_N%dup" % Nmin)
      formatCL(gCLA1s, "CLA1")
      gCLA1s.SetTitle("")
      gCLA1s.SetFillColor(3)
      gCLA1s.Draw("LF")
            
      gCL95 = infile.Get("CL95_N%dup" % Nmin)
      formatCL(gCL95, "CL95")
      gCL95.SetTitle("")
      gCL95.Draw("L")

      gCLA = infile.Get("CLA_N%dup" % Nmin)
      formatCL(gCLA, "CLA")
      gCLA.SetTitle("")
      gCLA.Draw("L")  
                
      label_11 = TPaveText(0.6616935,0.4076271,0.9193548,0.4605932,"brNDC")
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

         label_10 = TPaveText(0.636935,0.1264407,0.9314516,0.2109322,"brNDC")
         label_10.AddText(config.MI_old_label)
         label_10.SetTextSize(0.03813559);
         label_10.SetTextFont(42)
         label_10.SetFillColor(0)
         label_10.Draw("plain")
         gCLA_.SetLineStyle(10)
         store.append(label_10)


      gCLA2s.GetXaxis().SetRangeUser(1500, config.MI_maxST + 100)
      gCLA2s.GetYaxis().SetRangeUser(1e-4, 5.0)
      gCLA2s.GetYaxis().SetLabelSize(0.037)
      gCLA2s.GetYaxis().SetTitleSize(0.037)
      gCLA2s.GetYaxis().SetTitleOffset(1.18)

 
      cmslabel = TPaveText(0.45,0.90,0.60,0.93,"brNDC")
      cmslabel.AddText(config.cmsTitle)
      cmslabel.SetTextSize(0.041)
      #cmslabel.AddText(config.cmsSubtitle)
      cmslabel.SetFillColor(0)
      cmslabel.Draw("plain")
      store.append(cmslabel)

      legend = TLegend(0.4574194,0.6114407,0.8983871,0.8505932)
      legend.SetTextSize(0.04237288)
      legend.SetTextFont(42)
      legend.SetHeader("Multiplicity, N #geq %d" % Nmin)
      legend.AddEntry(gCL95, "Observed", "l")
      legend.AddEntry(gCLA1s, "Expected #pm 1#sigma", "lf")
      legend.AddEntry(gCLA2s, "Expected #pm 2#sigma", "lf")
      if Nmin <= config.MI_old_Nmin:
        legend.AddEntry(gCL95_, "Observed, 2011 data","l")
        legend.AddEntry(gCLA_, "Expected, 2011 data","l")
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
      c.Print("UpperLimits_Inclusive_Mul%d.png" % Nmin)
      c.Update()

   raw_input("Press Enter to continue...")

if __name__ == "__main__":
   main()
