import  csv
import random

f = open('교통사고정보1.csv','r')
rdr = csv.reader(f)

for line in rdr:


f.close()