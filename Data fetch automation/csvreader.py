import csv

readFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng\18100006.csv'
writeFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng\ml_18100006.csv'
with open(r'C:\Users\Adarsh\Downloads\18100006-eng\18100006.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        #print(row[0])
        #if row[0] > '2008-01':
         #   print(row[0], row[1], row[10], )

        if row[0] == '2018-09':
            print(row[0], row[3], row[10])
