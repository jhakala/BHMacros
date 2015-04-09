#!/bin/tcsh
source /uscms_data/d2/aferapon/BlackHolesAnalysis_8TeV/BHScripts_8TeV_postICHEP_Final_WithRun2012C_NewFitRange/setup.csh
cd /uscms_data/d2/aferapon/BlackHolesAnalysis_8TeV/BHScripts_8TeV_postICHEP_Final_WithRun2012C_NewFitRange/
#script you want to run (can be multiple commands)
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M4.0_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M4.0_Ms1.3_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M4.5_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M4.5_Ms1.3_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M5.0_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M5.0_Ms1.3_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M5.5_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M5.5_Ms1.3_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M6.0_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M6.0_Ms1.3_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M6.5_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M6.5_Ms1.3_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB4_BM-MD1.6_M7.0_Ms1.3_gs0.4.log -m SB4_BM-MD1.6_M7.0_Ms1.3_gs0.4
