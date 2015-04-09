./makeMIGraph.py -i MI-3.log -o MI-3.root -N 3
./makeMIGraph.py -i MI-4.log -o MI-4.root -N 4
./makeMIGraph.py -i MI-5.log -o MI-5.root -N 5
./makeMIGraph.py -i MI-6.log -o MI-6.root -N 6
./makeMIGraph.py -i MI-7.log -o MI-7.root -N 7
./makeMIGraph.py -i MI-8.log -o MI-8.root -N 8
rm MI.root
hadd MI.root MI-3.root MI-4.root MI-5.root MI-6.root MI-7.root MI-8.root
./plotModelIndependentLimits.py -i MI.root


