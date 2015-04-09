# =================
# General Setting
# =================
integrated_luminosity = 367. #pb-1
com = 8000 # GeV
cmsTitle = "CMS #sqrt{s} = %d TeV, %.1f fb^{-1}"\
   % (com / 1000.0, integrated_luminosity/1000.0)

#cmsSubtitle = "#sqrt{s} = %d TeV, %.1f fb^{-1}"\
#   % (com / 1000.0, integrated_luminosity/1000.0)

exclusive_multiplicities = [2, 3]
inclusive_multiplicities = [3, 4, 5, 6, 7, 8]

# ================================
# Settings for Background Template
#==================================
rebin = 10
fit_range = (1200., 2800.)
norm_range = (1800., 2200.)

# ================================
# Low range for MI plots
# ================================
low_bin = (1000,1000,1000,1200,1200,1200)

#p0:      '[0] * pow(1+x/7e3, [1]) / pow(x/7e3, [2] + [3]*log(x/7e3))',
#p1:      '[0] * pow(1 - x/7e3, [1]) / pow(x/7e3, [2] + [3]*log(x/7e3))',
#p2:      '[0] * pow(1 - x/7e3 + [3]*pow(x/7e3,2), [1]) / pow(x/7e3, [2])',
#p3:      '[0] * pow(1 - x/7e3, [1]) / pow(x/7e3, [2])',      
#p4:      '[0] / pow([1] + [2]*x*1e-3 + x*x*1e-6,[3])',
#p5:      '[0] / pow([1] + x/7e3, [2])'  

# Dijet Parameterizations

templates = [
      '[0] * pow(1 + x/8e3, [1]) / pow(x/8e3, [2] + [3]*log(x/8e3))',
#      '[0] * pow(1 - x/7e3, [1]) / pow(x/7e3, [2] + [3]*log(x/7e3))',
#      '[0] * pow(1 - x/7e3 + [3]*pow(x/7e3,2), [1]) / pow(x/7e3, [2])'# ,
#      '[0] * pow(1 - x/7e3, [1]) / pow(x/7e3, [2])',      
      '[0] / pow([1] + [2]*x*1e-3 + x*x*1e-6,[3])',
      '[0] / pow([1] + x/8e3, [2])'     
      ]      
      
# Old Parametrizations
#templates = [
#      '[0] * pow(1+x/7e3, [1]) / pow(x/7e3, [2] + [3]*log(x/7e3))',
#      '[0] / pow([1] + [2]*x*1e-3 + x*x*1e-6,[3])',
#      '[0] / pow([1] + x/7e3, [2])']

label_for_data = []
label_for_ref = []
for N in exclusive_multiplicities:
   label_for_data.append("%s" % N)
   label_for_ref.append("%s" % N)
for N in inclusive_multiplicities:
   label_for_data.append("%sup" % N)

# =====================================
# Settings for Model Independent Limits
# =====================================
relative_luminosity_uncertainty = 0.045
nominal_signal_uncertainty = 0.05

MI_old_file = "ModelIndependentLimits2011.root"
MI_old_label = "2011, 4.7 fb^{-1}"
MI_old_Nmin = 8
MI_new_label = "2012, %.1f fb^{-1}" % (integrated_luminosity * 1e-3)
MI_maxST = 5000.


# ==================
# Settings for Plots
# ==================
maxST = 5550.

bh_dir = "histograms/BH_52X"
bh_xsec = "XsecTables_8TeV_MSTW/TheoreticalXsec.root"
bh_list = "models52X.txt"

sm_dir = ""
sm_models = []
sm_colors = []

bh_showcase = ["BH1_BM-MD1.5_M5.5_n6",
   "BH1_BM-MD2.0_M5.0_n4",
   "BH1_BM-MD2.5_M4.5_n2"]

limit_showcase = ["BH1_BM-MD2.5_n2",
   "BH1_BM-MD2.0_n4",
   "BH1_BM-MD1.5_n6"]

model_description = {
      "BH1_BM":"Nonrotating",
      "BH2_BM":"Rotating",
      "BH5_BM":"Rotating (mass and angular momentum loss)",
      "BH2_CH":"Rotating",
      "BH4_CH":"Nonrotating",
      "BH6_CH":"Rotating (Yoshino-Rychkov loss)",
      "BH8_CH":"Rotating, low multiplicity regime",
      "BH9_CH":"Boiling Remnant (Yoshino-Rychkov loss)",
      "BH10_CH":"Stable Remnant (Yoshino-Rychkov loss)",
      "SB4_BM":"M_{D} = 1.6 TeV, M_{s} = 1.3 TeV, g_{s} = 0.4",
      "SB6_BM":"M_{D} = 2.1 TeV, M_{s} = 1.7 TeV, g_{s} = 0.4",
      "SB2_BM":"M_{D} = 1.3 TeV, M_{s} = 1.0 TeV, g_{s} = 0.4"
}

class Summary:
   def __init__(self, name, generator, n, models):
      self.name = name 
      self.generator = generator
      self.n = n
      self.models = models

summary_list = [
      Summary("BlackMax", "BM", [2,4,6], ["BH1","BH2","BH5"]),
      Summary("Charybdis", "CH", [2,4,6], ["BH2","BH4","BH6","BH8","BH9","BH10"])
      ]

extraDim_list = [2, 4, 6]
#MD_list = [1.5, 2.0, 2.5, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
MD_list = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
