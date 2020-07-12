from Kinematics import *
import csv

print("Please drag and drop your .csv file into the terminal")
#studentInfo = input()
studentInfo = "SPH3U1-01_2019_.csv"
#with open('SPH3U1-02_2018_.csv', 'r') as file:
with open(studentInfo, 'r') as file:
    # Initializing and formatting export data
    fileReader = csv.reader(file)
    fileData = list(fileReader)
    n = 0
    for lines in fileData:
        del lines[-1]

    title = ["Q1 Text", "Q1 Answer", "Q2 Text", "Q2 Answer"]
    # Populating export data and writing .tex file
    for line in fileData:
        if n == 0:
            for i in title:
                fileData[0].append(i)
            n = n + 1
        else:
            q = Kinematics()
            data = [q.get_q1(), q.solution_1, q.get_q2(), q.solution_2]
            for i in data:
                line.append(i)
            q.LaTeXWriter(line)
    
    # Exporting data
    writeFile = open('Kinematics Randomized Results.csv', 'w')
    writer = csv.writer(writeFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in fileData:
        writer.writerow(row)

    writeFile.close()
    file.close()

print("Program Terminated")