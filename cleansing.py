import os
import random
import shutil

# give random seed
random.seed(123)

# define the original path of files
root_dir = '/home/yu/Desktop/title'# path of working directory
image_dir = os.path.join(root_dir, 'images') 
label_dir = os.path.join(root_dir, 'labels')
output_dir = '/home/yu/Desktop/yolov8_dataset'# path of output directory

# define the ratio of train/valid/test
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

# get the filename of image/txt files
image_filenames = [os.path.splitext(f)[0] for f in os.listdir(image_dir)]
label_filenames = [os.path.splitext(f)[0] for f in os.listdir(label_dir)]

# randomize the file list
random.shuffle(image_filenames)

# calculate the number of files for each classification
total_count = len(image_filenames)
train_count = int(total_count * train_ratio)
valid_count = int(total_count * valid_ratio)
test_count = total_count - train_count - valid_count

# define the output directory
train_image_dir = os.path.join(output_dir, 'train', 'images')
train_label_dir = os.path.join(output_dir, 'train', 'labels')
valid_image_dir = os.path.join(output_dir, 'valid', 'images')
valid_label_dir = os.path.join(output_dir, 'valid', 'labels')
test_image_dir = os.path.join(output_dir, 'test', 'images')
test_label_dir = os.path.join(output_dir, 'test', 'labels')

# create the above directories
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(valid_image_dir, exist_ok=True)
os.makedirs(valid_label_dir, exist_ok=True)
os.makedirs(test_image_dir, exist_ok=True)
os.makedirs(test_label_dir, exist_ok=True)

# division
for i, filename in enumerate(image_filenames):
    if i < train_count:
        output_image_dir = train_image_dir
        output_label_dir = train_label_dir
    elif i < train_count + valid_count:
        output_image_dir = valid_image_dir
        output_label_dir = valid_label_dir
    else:
        output_image_dir = test_image_dir
        output_label_dir = test_label_dir

    # copy image files
    src_image_path = os.path.join(image_dir, filename + '.png')
    dst_image_path = os.path.join(output_image_dir, filename + '.png')
    shutil.copy(src_image_path, dst_image_path)

    # copy txt files
    src_label_path = os.path.join(label_dir, filename + '.txt')
    dst_label_path = os.path.join(output_label_dir, filename + '.txt')
    shutil.copy(src_label_path, dst_label_path)
