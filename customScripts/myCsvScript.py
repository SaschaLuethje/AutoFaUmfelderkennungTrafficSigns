# The csv file of the GTSRB file contains all images. This script devides the csv file into multiple ones, one for every image.
# usage: for example $ python myCsvScript.py 'GT-00014.csv' 'Stop'

import sys

csvInputFileName = sys.argv[1]
className = sys.argv[2]<

with open(csvInputFileName, 'r') as file:
    data = file.read().split('\n')
    for line in data:
        fileName = line.split(';')[0]

        # Replace ClassID with ClassName
        lengthOfClassID = len(line.split(';')[-1])
        line = line[:-lengthOfClassID] # Drop ClassID
        line = line + className # Add ClassName

        # Do not know why, but csv files should use ',' as seperator and the given csv uses ';'. Therefore, we replace this.
        line = line.replace(";", ",")

        # We have converted the images from ppm to jpg in a previous step. Therefore we need to change it here also.
        line = line.replace("ppm", "jpg")
        
        fileNameWithoutExtension = fileName.split('.')[0]
        fileNameCSV = fileNameWithoutExtension + ".csv"
        f = open(fileNameCSV, "x")
        f.write(line)
        f.close()