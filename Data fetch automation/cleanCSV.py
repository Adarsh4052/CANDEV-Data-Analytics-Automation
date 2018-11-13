import csv
readFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng\18100006.csv'
writeFilePath = r'C:\Users\Adarsh\Downloads\18100006-eng\ml_18100006.csv'
writeFilePath_vis = r'C:\Users\Adarsh\Downloads\18100006-eng\vis_18100006.csv'

#row1 = ['date', 'Product Groups', 'Consumer Price Index']
with open(readFilePath, 'r', newline='') as readFile, open(writeFilePath, 'a', newline='') as writeFile, \
        open(writeFilePath_vis, 'a', newline='') as writeFile_vis:
    next(readFile)  # Skip over header in input file.
    readCSV = csv.reader(readFile, delimiter=',')

#for machine learning
    for row in readCSV:
        if ( (row[0] > '2008-09')
                & (row[3] in ('All-items', 'Food' , 'Shelter' , 'Transportation'))):
            #writer.writerows(line.split() for line in readFile)
            #print(row[0], row[3], row[10])
            line = [row[0], row[3], row[10]]
            print(line)
            writer = csv.writer(writeFile)
            writer.writerow(line)
        print("ML csv file has been written!")
        print("Writing vis file...")
        # for visualization
        if ( (row[0] > '2016-09')
                & (row[3] in ('All-items', 'Food' , 'Shelter' , 'Transportation'))):
            #writer.writerows(line.split() for line in readFile)
            #print(row[0], row[3], row[10])
            line = [row[0], row[3], row[10]]
            print(line)
            writer = csv.writer(writeFile_vis)
            writer.writerow(line)

