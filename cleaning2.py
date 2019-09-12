# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:47:16 2019

@author: cmaug
"""

import csv

output = []
qbs = []
header = []
with open('NFL Play by Play 2009-2018 (v5).csv') as f:
    reader = csv.reader(f)
    line = 0
    for row in reader:
        if line == 0:
            output.append(row)
            line += 1
        else:
            if row[25] == 'pass':
                output.append(row)
            line += 1
        print(line)
with open('updated2.csv',"w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(output)
print('done')