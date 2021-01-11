from PIL import Image 
import glob, os
import sys

target_directory = sys.argv[1]

for infile in glob.glob(os.path.join(target_directory, "*.ppm")):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.save(file + ".jpg")