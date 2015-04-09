import csv
with open('xsec_table.txt', 'rb') as f:
   reader = csv.reader(f, delimiter=" ")
   for r in reader:
      print r
