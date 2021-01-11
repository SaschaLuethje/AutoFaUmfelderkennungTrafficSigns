import sys
import os

newFile = open('combinedCSV.csv', 'x')
newFile.write('filename,width,height,xmin,ymin,xmax,ymax,class')
newFile.write('\n')
completeCsvFile = open('GT-00014.csv')
completeCsvData = completeCsvFile.read().split('\n')
for file in os.listdir("."):
    if file.endswith(".jpg"):
        with open(file, 'r') as file:
            data = file.read()
            fileName = data.split('')
            newFile.write(data)
            newFile.write('\n')
newFile.close()