# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import expanddouban
import urllib
import csv
import collections
import operator 
from copy import deepcopy

movieList = []
with open('movies.csv', newline='',encoding='utf-8-sig') as csvfile:
     spamreader = csv.reader(csvfile, delimiter='|')
     for row in spamreader:
         movieList.append(row)
#print(movieList)

d = collections.defaultdict(int)
for item in movieList:
	d[item[3]] += 1
print(d)
d2 = collections.defaultdict(dict)
d3 = collections.defaultdict(int)
for item in movieList:
	d2[item[3]] = deepcopy(d3)
for item in movieList:
	d2[item[3]][item[2]] += 1
#print(d2)
rankList = []
for item in d2:
	rankSubList = [item,]
	#print(item,":",sorted(d2[item].values()))
	for (key,value) in sorted(d2[item].items(),key=operator.itemgetter(1),reverse=True): 
		rankSubList.append((key,value,"占比:"+str(round(value/d[item]*100,2))+"%"))
	rankList.append(rankSubList)
	#print(operator.itemgetter(1))

with open("output.txt","w",encoding='utf-8-sig') as f:
	for item in rankList:
		f.write(str(item[0:4])+"\n")
#print(d2)