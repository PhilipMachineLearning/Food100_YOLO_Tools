# food100_split_for_yolo.py
#
# This script will split the food100 dataset into 2 files of images list
# accourding to the 'percentage_test'. The default is 10% will be assigned to test.
# (1) train.txt - the list of training images
# (2) test.txt - the list of validating images
#
# Credit: script is originated from blob post description
# <https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/>
#
import glob, os
from pathlib import Path

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
#path_data = 'data/food100/'
path_data = str(Path.cwd().parent.resolve() / 'data' / 'food100')

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
#file_train = open('train.txt', 'w')
#file_test = open('test.txt', 'w')

file_train = open(str(Path.cwd().resolve() / 'Food100_YOLO_Tools' / 'train.txt'), 'w')
file_test = open(str(Path.cwd().resolve() / 'Food100_YOLO_Tools' / 'test.txt'), 'w')

print(f"file_train path: {file_train}")
print(f"file_train path: {file_test}")

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "images/*/*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(f"Path and File name: {pathAndFilename}") 

    if counter == index_test:
        counter = 1
        #file_test.write(path_data + title + '.jpg' + "\n")
        file_test.write(pathAndFilename + "\n")
    else:
        #file_train.write(path_data + title + '.jpg' + "\n")
        file_train.write(pathAndFilename + "\n")
        counter = counter + 1
