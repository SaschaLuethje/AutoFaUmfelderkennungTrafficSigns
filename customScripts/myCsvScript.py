# The csv file of the GTSRB file contains all images. This script devides the csv file into multiple ones, one for every image.
# usage: for example $ python myCsvScript.py 'GT-00014.csv'

import sys

csvInputFileName = sys.argv[1]

with open(csvInputFileName, 'r') as file:
    data = file.read().split('\n')
    for line in data:
        fileName = line.split(';')[0]
        fileNameWithoutExtension = fileName.split('.')[0]
        fileNameCSV = fileNameWithoutExtension + ".csv"
        f = open(fileNameCSV, "x")
        f.write(line)
        f.close()