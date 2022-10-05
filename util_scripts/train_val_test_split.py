### Python script to split a labeled image dataset into Train, Validation, and Test folders.
# Author: Evan Juras, EJ Technology Consultants
# Date: 4/10/21

# Randomly splits images to 80% train, 10% validation, and 10% test, and moves them to their respective folders. 
# This script is intended to be used in the TFLite Object Detection Colab notebook here:
# https://colab.research.google.com/github/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi/blob/master/Train_TFLite2_Object_Detction_Model.ipynb

import glob
import random
import os

# Define paths to image folders
image_path = '/content/images/all'
train_path = '/content/images/train'
val_path = '/content/images/validation'
test_path = '/content/images/test'

# Get list of all images
jpg_file_list = glob.glob(image_path + '/*.jpg')
JPG_file_list = glob.glob(image_path + '/*.JPG')
png_file_list = glob.glob(image_path + '/*.png')
bmp_file_list = glob.glob(image_path + '/*.bmp')

file_list = jpg_file_list + JPG_file_list + png_file_list + bmp_file_list
file_num = len(file_list)
print('Total images: %d' % file_num)

# Determine number of files to move to each folder
train_percent = 0.8  # 80% of the files go to train
val_percent = 0.1 # 10% go to validation
test_percent = 0.1 # 10% go to test
train_num = int(file_num*train_percent)
val_num = int(file_num*val_percent)
test_num = file_num - train_num - val_num
print('Files moving to train: %d' % train_num)
print('Files moving to validation: %d' % val_num)
print('Files moving to test: %d' % test_num)

# Select 80% of files randomly and move them to train folder
for i in range(train_num):
    move_me = random.choice(file_list)
    fn = move_me.split('/')[-1]
    base_fn = fn[:(len(fn)-4)] # Gets rid of .jpg, .png, or .bmp at end of the string
    xml_fn = base_fn + '.xml'
    os.rename(move_me, train_path+'/'+fn)
    os.rename(os.path.join(image_path,xml_fn),os.path.join(train_path,xml_fn))
    file_list.remove(move_me)

# Select 10% of remaining files and move them to validation folder
for i in range(val_num):
    move_me = random.choice(file_list)
    fn = move_me.split('/')[-1]
    base_fn = fn[:(len(fn)-4)] # Gets rid of .jpg, .png, or .bmp at end of the string
    xml_fn = base_fn + '.xml'
    os.rename(move_me, val_path+'/'+fn)
    os.rename(os.path.join(image_path,xml_fn),os.path.join(val_path,xml_fn))
    file_list.remove(move_me)

# Move remaining files to test folder
for i in range(test_num):
    file = file_list[i]
    fn = file.split('/')[-1]
    base_fn = fn[:(len(fn)-4)] # Gets rid of .jpg, .png, or .bmp at end of the string
    xml_fn = base_fn + '.xml'
    os.rename(file, test_path+'/'+fn)
    os.rename(os.path.join(image_path,xml_fn),os.path.join(test_path,xml_fn))
