#!/bin/tcsh
source /uscms_data/d2/aferapon/BlackHolesAnalysis_8TeV/BHScripts_8TeV_postICHEP_Final_WithRun2012C_NewFitRange/setup.csh
cd /uscms_data/d2/aferapon/BlackHolesAnalysis_8TeV/BHScripts_8TeV_postICHEP_Final_WithRun2012C_NewFitRange/
#script you want to run (can be multiple commands)
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M4.0_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M4.0_Ms1.7_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M4.5_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M4.5_Ms1.7_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M5.0_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M5.0_Ms1.7_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M5.5_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M5.5_Ms1.7_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M6.0_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M6.0_Ms1.7_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M6.5_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M6.5_Ms1.7_gs0.4
./calModelXsecLimits.py -i Templates.root -o significance.root -l SB6_BM-MD2.1_M7.0_Ms1.7_gs0.4.log -m SB6_BM-MD2.1_M7.0_Ms1.7_gs0.4
