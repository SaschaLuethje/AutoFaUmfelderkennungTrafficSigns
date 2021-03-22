import sys
import xml.etree.ElementTree as ET
import lxml.builder
import codecs
from xml.dom import minidom


def addObject(ROOT, className, xmin, ymin, xmax, ymax):
    OBJ = ET.SubElement(ROOT, 'object')
    CLASS = ET.SubElement(OBJ, 'name')
    CLASS.text = className
    POSE = ET.SubElement(OBJ, 'pose')
    POSE.text = 'unspecified'
    TRUN = ET.SubElement(OBJ, 'truncated')
    TRUN.text = '0'
    DIF = ET.SubElement(OBJ, 'difficult')
    DIF.text = '0'
    BOX = ET.SubElement(OBJ, 'bndbox')
    XMIN = ET.SubElement(BOX, 'xmin')
    XMIN.text = xmin
    YMIN = ET.SubElement(BOX, 'ymin')
    YMIN.text = ymin
    XMAX = ET.SubElement(BOX, 'xmax')
    XMAX.text = xmax
    YMAX = ET.SubElement(BOX, 'ymax')
    YMAX.text = ymax

    return OBJ

def createRoot(fileName):
    ROOT = ET.Element("annotation")
    FNAME = ET.SubElement(ROOT, 'filename')
    FNAME.text = fileName
    FOLDER = ET.SubElement(ROOT, 'folder')
    FOLDER.text = 'AutoFa'
    SRC = ET.SubElement(ROOT, 'source')
    DB = ET.SubElement(SRC, 'database')
    DB.text = 'AutoFa'
    ANT = ET.SubElement(SRC, 'annotation')
    ANT.text = 'custom'
    IMG = ET.SubElement(SRC, 'image')
    IMG.text = 'custom'

    return ROOT

# csvInputFileName = sys.argv[1]
csvInputFileName = "test.csv"
tempFileName = None

E = lxml.builder.ElementMaker()

with open(csvInputFileName, 'r') as file:
    data = file.read().split('\n')
    for line in data:
        
        # load line
        fileName = line.split(',')[0]
        width = line.split(',')[1]
        height = line.split(',')[2]
        xmin = line.split(',')[3]
        ymin = line.split(',')[4]
        xmax = line.split(',')[5]
        ymax = line.split(',')[6]
        className = line.split(',')[7]

        if tempFileName != None and tempFileName != fileName:
            fileNameWithoutExtension = tempFileName.split('.')[0]
            # myData = ET.tostring(ROOT, pretty_print=True , encoding="unicode")
            myData = minidom.parseString(ET.tostring(ROOT)).toprettyxml(indent="   ")
            myFile = open(fileNameWithoutExtension + ".xml", "w")
            myFile.write(myData)
            myFile.close()

        if tempFileName != fileName:
            ROOT = createRoot(fileName)
        
        OBJ = addObject(ROOT, className, xmin, ymin, xmax, ymax)

        tempFileName = fileName

