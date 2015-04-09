#cat BH*log | grep -v 'MD4.5' | grep -v 'BH10_CH-MD4.0' > XsecLimits.txt
cat BH*log > XsecLimits.txt
./makeXsecLimitsRoot.py -i XsecLimits.txt -o XsecLimits.root
