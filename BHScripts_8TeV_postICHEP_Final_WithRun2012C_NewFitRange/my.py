#!/usr/bin/env python################################################## Parse text from input files## Gena Kukartsev, September 2011#################################################import fileinputimport systexfile = open("tableModel.tex","w")
for line in fileinput.input():    #print line.strip()    _words = line.strip().split()    #print _words    # skip empty lines    if len(_words) == 0:        continue    # find substring
    pos1 = _words[0].find('MD',0) + 2    pos2 = _words[0].find('_',pos1)    pos3 = pos2 + 5
    pos4 = pos3 + 4

    pos5 = float(_words[1])
    pos6 = int(_words[2])
    pos7 = int(_words[3])
    pos8 = float(_words[4])
    pos9 = float(_words[5])
    pos10 = int(_words[6])
    pos11 = float(_words[7]) #pm pos12
    pos12 = float(_words[8]) 
    pos13 = float(_words[9])
    pos14 = float(_words[10]) 
    print _words[0][pos1:pos2], "&", _words[0][pos2+2:pos3], "&",_words[0][pos3+2:pos4],"&", pos5, "&", pos6,"&", pos7, "&", pos8,"&", pos9, "&", pos10,"&", pos11, "&", pos12, "&", pos13, "&", pos14, "\\\\"      
    #texfile.write("%f" % pos5)

    if pos12 > pos11:
       texfile.write("%.1f & %.1f & %i & %f & %i & %.1f & %.1f & %.2f & %i & $%.3f ^{+%.3f}_{-%.3f}$ & %.4f & %.4f\\\\\n" % (float(_words[0][pos1:pos2].strip()), float(_words[0][pos2+2:pos3].strip()), int(_words[0][pos3+2:pos4].strip()),pos5,pos6,pos7/1000.,pos8*100.,pos9,pos10,pos11,pos12,pos11,pos13,pos14))
    else:
       texfile.write("%.1f & %.1f & %i & %f & %i & %.1f & %.1f & %.2f & %i & $%.3f \pm %.3f$ & %.4f & %.4f\\\\\n" % (float(_words[0][pos1:pos2].strip()), float(_words[0][pos2+2:pos3].strip()), int(_words[0][pos3+2:pos4].strip()),pos5,pos6,pos7/1000.,pos8*100.,pos9,pos10,pos11,pos12,pos13,pos14))
