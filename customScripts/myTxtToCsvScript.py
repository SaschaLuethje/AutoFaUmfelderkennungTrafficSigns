# The csv file of the GTSRB file contains all images. This script devides the csv file into multiple ones, one for every image.
# usage: for example $ python myCsvScript.py 'GT-00014.csv' 'Stop'

import sys

with open('gt.txt', 'r') as file:
    classDictrionary = {
        0: "speed limit 20 (prohibitory)",
        1: "speed limit 30 (prohibitory)",
        2: "speed limit 50 (prohibitory)",
        3: "speed limit 60 (prohibitory)",
        4: "speed limit 70 (prohibitory)",
        5: "speed limit 80 (prohibitory)",
        6: "restriction ends 80 (other)",
        7: "speed limit 100 (prohibitory)",
        8: "speed limit 120 (prohibitory)",
        9: "no overtaking (prohibitory)",
        10: "no overtaking (trucks) (prohibitory)",
        11: "priority at next intersection (danger)",
        12: "priority road (other)",
        13: "give way (other)",
        14: "stop (other)",
        15: "no traffic both ways (prohibitory)",
        16: "no trucks (prohibitory)",
        17: "no entry (other)",
        18: "danger (danger)",
        19: "bend left (danger)",
        20: "bend right (danger)",
        21: "bend (danger)",
        22: "uneven road (danger)",
        23: "slippery road (danger)",
        24: "road narrows (danger)",
        25: "construction (danger)",
        26: "traffic signal (danger)",
        27: "pedestrian crossing (danger)",
        28: "school crossing (danger)",
        29: "cycles crossing (danger)",
        30: "snow (danger)",
        31: "animals (danger)",
        32: "restriction ends (other)",
        33: "go right (mandatory)",
        34: "go left (mandatory)",
        35: "go straight (mandatory)",
        36: "go right or straight (mandatory)",
        37: "go left or straight (mandatory)",
        38: "keep right (mandatory)",
        39: "keep left (mandatory)",
        40: "roundabout (mandatory)",
        41: "restriction ends (overtaking) (other)",
        42: "restriction ends (overtaking (trucks)) (other)"
    }
    data = file.read().split('\n')
    f = open('MyNewCSVFile', "x")
    headerLine = "filename,width,height,xmin,ymin,xmax,ymax,class\n"
    f.write(headerLine)
    for line in data:
        fileName = line.split(';')[0].split('.')[0] + ".jpg"
        image = cv2.imread(fileName)
        height = np.size(image, 0)
        width = np.size(image, 1)

        # Replace ClassID with ClassName
        classID = line.split(';')[-1]
        line = line[:-lengthOfClassID] # Drop ClassID
        className = classDictrionary[classID] # Get ClassName from dictionary

        myNewLine = filename + "," + height + "," + width + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + className + '\n'
        
        f.write(line)
    f.close()