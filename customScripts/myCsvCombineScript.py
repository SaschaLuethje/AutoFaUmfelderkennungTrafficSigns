import sys
import os

# inputDic = sys.argv[1]

newFile = open('combinedCSV.csv', 'x')
newFile.write('filename,width,height,xmin,ymin,xmax,ymax,class')
newFile.write('\n')
for file in os.listdir('../images/train'):
    if file.endswith(".csv"):
        with open(file, 'r') as file:
            data = file.read()
            newFile.write(data)
            newFile.write('\n')
newFile.close()