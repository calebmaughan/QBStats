# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:37:05 2019

@author: cmaug
"""
import random
import csv
import numpy
from pathlib import Path



scores = [0] * 33
time = [0] * 901
for i in range(901):
    if i < 33:
        if i < 9:
            scores[i] = 1
        elif i < 17:
            scores[i] = 2
        elif i < 25:
            scores[i] = 3
        else:
            scores[i] = 4
    if i < 119:
        time[i] = 1
    elif i < 360:
        time[i] = 2
    elif i < 659:
        time[i] = 3
    else:
        time[i] = 4
clutch = []
regular = []
header = []
output = []
output.append(['Quarterback', 'Set', 'Atts', 'Percentage', 'YPA', 'Touchdowns', 'Ints', 'Sacks'])

pathlist = Path('qbs').glob('**/*.csv')
#for i in range (1):
for path in pathlist:
    print(str(path))

    with open(str(path)) as f:
    #with open('qbs/A.Smith.csv') as f:
        clutch = []
        regular = []
        reader = csv.reader(f)
        line = 0
        for row in reader:
            if line == 0:
                header = row
                line += 1
            else:
                try:
                    scoreDiff = int(row[51]) - int(row[50])
                    if scoreDiff >= 0 and scoreDiff < 33:
                        scoreDiff = scores[scoreDiff]
                        timeLeft = float(row[12])
                        timeLeft = int(timeLeft)
                        if timeLeft > 0 and timeLeft < 901:
                            timeLeft = time[timeLeft]
                            if scoreDiff == timeLeft:
                                clutch.append(row)
                            else:
                                regular.append(row)
                    else:
                        regular.append(row)
                    line += 1
                except:
                    print('skipped')
    if line >= 400:
        allPassesarr = []
        completedPassesarr = []
        sacksarr = []
        interceptionsarr = []
        totalYardsarr = []
        airYardsarr = []
        touchdownsarr = []
        completionPercentage = []
        ypa = []
        
        callPasses = 0
        ccompletedPasses = 0
        csacks = 0
        cinterceptions = 0
        ctotalYards = 0
        cairYards = 0
        ctouchdowns = 0
        
        for row in clutch:
            if line == 0:
                line += 1
            else:
                if int(row[154]) == 1:
                    callPasses += 1
                    ccompletedPasses += 1
                    ctotalYards += int(row[26])
                    if int(row[144]) == 1:
                        ctouchdowns += 1
                if int(row[118]) == 1:
                    callPasses += 1
                if int(row[119]) == 1:
                    cinterceptions += 1
                    callPasses += 1                
                if row[42] == 'failure':
                    callPasses += 1
                if row[42] == 'success':
                    callPasses += 1
                    ccompletedPasses += 1
                    ctotalYards += 2
                if int(row[143]) == 1:
                    csacks += 1
        
        #for row in regular:
        #    if line == 0:
        #        line += 1
        #    else:
        #        if int(row[154]) == 1:
        #            allPasses += 1
        #            completedPasses += 1
        #            totalYards += int(row[26])
        #            airYards += int(row[35])
        #            if int(row[144]) == 1:
        #                touchdowns += 1
        #        if int(row[118]) == 1:
        #            allPasses += 1
        #        if int(row[119]) == 1:
        #            interceptions += 1
        #            allPasses += 1                
        #        if row[42] == 'failure':
        #            allPasses += 1
        #        if row[42] == 'success':
        #            allPasses += 1
        #            completedPasses += 1
        #            totalYards += 2
        #        if int(row[143]) == 1:
        #            sacks += 1
        for i in range(50000):
            allPasses = 0
            completedPasses = 0
            sacks = 0
            interceptions = 0
            totalYards = 0
            airYards = 0
            touchdowns = 0
            mysample = random.sample(regular, len(clutch))
            for row in mysample:
                if line == 0:
                    line += 1
                else:
                    if int(row[154]) == 1:
                        allPasses += 1
                        completedPasses += 1
                        totalYards += int(row[26])
                        if int(row[144]) == 1:
                            touchdowns += 1
                    if int(row[118]) == 1:
                        allPasses += 1
                    if int(row[119]) == 1:
                        interceptions += 1
                        allPasses += 1                
                    if row[42] == 'failure':
                        allPasses += 1
                    if row[42] == 'success':
                        allPasses += 1
                        completedPasses += 1
                        totalYards += 2
                    if int(row[143]) == 1:
                        sacks += 1
            allPassesarr.append(allPasses)
            completedPassesarr.append(completedPasses)
            sacksarr.append(sacks)
            interceptionsarr.append(interceptions)
            totalYardsarr.append(totalYards)
            #airYardsarr.append(airYards)
            touchdownsarr.append(touchdowns)
            if allPasses > 0:
                completionPercentage.append(completedPasses/allPasses)
                ypa.append(totalYards/allPasses)
            else:
                completionPercentage.append(0)
                ypa.append(0)
            
        
        meanAtts = numpy.mean(allPassesarr)
        SEAtts = numpy.std(allPassesarr)
        meanComps = numpy.mean(completedPassesarr)
        SEComps = numpy.std(completedPassesarr)
        meanSacks = numpy.mean(sacksarr)
        SESacks = numpy.std(sacksarr)
        meanTDs = numpy.mean(touchdownsarr)
        SETDs = numpy.std(touchdownsarr)
        meanPer = numpy.mean(completionPercentage)
        SEPer = numpy.std(completionPercentage)
        meanInts = numpy.mean(interceptionsarr)
        SEInts = numpy.std(interceptionsarr)
        meanYPA = numpy.mean(ypa)
        SEYPA = numpy.std(ypa)
        zscore = 1.645
        
        TSSacks = meanSacks - (zscore * SESacks)
        TSTDs = meanTDs + (zscore * SETDs)
        percentage = ccompletedPasses/callPasses
        TSPer = meanPer + (zscore * SEPer)
        TSInts = meanInts - (zscore * SEInts)
        cypa = ctotalYards/callPasses
        TSYPA = meanYPA + (zscore * SEYPA)
        
        sacksarr = sorted(sacksarr, reverse = True)
        touchdownsarr = sorted(touchdownsarr)
        completionPercentage = sorted(completionPercentage)
        interceptionsarr = sorted(interceptionsarr, reverse = True)
        ypa = sorted(ypa)
        allPassesarr = sorted(allPassesarr)
        
        qb = clutch[0][161]
        
        output.append([qb, 'Sample', meanAtts, meanPer, meanYPA, meanTDs, meanInts, meanSacks])
        output.append([qb, 'Clutch', callPasses, ccompletedPasses/callPasses, ctotalYards/callPasses, ctouchdowns, cinterceptions, csacks])
        output.append([qb, 'SD Cutoff', meanAtts, TSPer, TSYPA, TSTDs, TSInts, TSSacks])
        output.append([qb, 'Pure Cutoff', allPassesarr[25000], completionPercentage[47500], ypa[47500], touchdownsarr[47500], interceptionsarr[47500], sacksarr[47500]])
        output.append([])
        
#        print('Standard Deviation')
#        print('Sacks:', TSSacks)
#        print('TDs:', TSTDs)
#        print('Percentage:', TSPer)
#        print('Ints:', TSInts)
#        print('YPA:', TSYPA)
#        print('')
#        
#        print('Pure Cutoff')
#        print('Sacks:', sacksarr[4750])
#        print('TDs:', touchdownsarr[4750])
#        print('Percentage:', completionPercentage[4750])
#        print('Ints:', interceptionsarr[4750])
#        print('YPA:', ypa[4750])
#        
#        print('')
#        print(callPasses)
#        print(ccompletedPasses)
#        print('sacks:', csacks)
#        print('touchdowns', ctouchdowns)
#        print('percentage', ccompletedPasses/callPasses)
#        print('ints', cinterceptions)
#        print('ypa', ctotalYards/callPasses)
#        
#        print('')
#        print('sample')
#        print(numpy.mean(allPassesarr))
#        print(numpy.mean(completedPassesarr))
#        print(numpy.mean(sacksarr))
#        print(numpy.mean(touchdownsarr))
#        print(numpy.mean(completionPercentage))
#        print(numpy.mean(interceptionsarr))
#        print(numpy.mean(ypa))
    else:
        print('skip')
        
#with open('qbs/Rodgers/clutch.csv') as f:
#    reader = csv.reader(f)
#    line = 0
#    for row in reader:
#        if line == 0:
#            line += 1
#        else:
#            if int(row[154]) == 1:
#                callPasses += 1
#                ccompletedPasses += 1
#                ctotalYards += int(row[26])
#                cairYards += int(row[35])
#                if int(row[144]) == 1:
#                    ctouchdowns += 1
#            if int(row[118]) == 1:
#                callPasses += 1
#                if int(row[119]) == 1:
#                    cinterceptions += 1
#            if int(row[143]) == 1:
#                csacks += 1
    with open('final.csv',"w+", newline='') as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(output)
print('done')    
