import csv

output = [[]]
qbs = []
header = []
with open('updated2.csv') as f:
    reader = csv.reader(f)
    line = 0
    for row in reader:
        if line == 0:
            header = row
            line += 1
        else:
            if row[161] in qbs:
                output[qbs.index(row[161])].append(row)
            else:
                qbs.append(row[161])
                output.append([])
                output[qbs.index(row[161])].append(row)
            line += 1
        print(line)
for i in range(len(output) - 1):
    temp = []
    temp.append(header)
    temp.append(output[i])
    print(output[i][0][161])
    print(qbs[i])
    path = 'qbs/' + str(qbs[i]) + '.csv'
    with open(path,"w+", newline='') as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerow(temp[0])
        csvWriter.writerows(temp[1])

print('done')