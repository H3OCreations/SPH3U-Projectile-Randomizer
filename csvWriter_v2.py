from Projectile import *
import csv

print("Please drag and drop your .csv file into the terminal")
#studentInfo = input()
studentInfo = "SPH3U1-02_2018_.csv"
#with open('SPH3U1-02_2018_.csv', 'r') as file:
with open(studentInfo, 'r') as file:
    # Initializing and formatting export data
    fileReader = csv.reader(file)
    fileData = list(fileReader)
    n = 0
    for lines in fileData:
        del lines[-1]

    title = ["velocity", "angle", "max height", "range", "time", "building height", "building max height", "building range", "building time"]

    # Populating export data and writing .tex file
    for line in fileData:
        if n == 0:
            for i in title:
                fileData[0].append(i)
            n = n + 1
        else:
            q = Projectile()
            data = [q.vi, q.theta, q.getMaxHeight(), q.getRange(), q.getFlightTime(), q.buildingHeight, q.getBuildingMaxHeight(), q.getBuildingRange(), q.getBuildingFlightTime()]
            for i in data:
                line.append(i)
            q.LaTeXWriter(line)
    
    # Exporting data
    writeFile = open('Projectile Randomized Results.csv', 'w')
    writer = csv.writer(writeFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in fileData:
        writer.writerow(row)

    writeFile.close()
    file.close()

print("Program Terminated")