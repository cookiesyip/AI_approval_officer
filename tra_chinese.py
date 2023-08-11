#generate the label file from the filename

#migrate all the data together and divide them into 3 parts

#generate new groups 


import os
import random
import shutil
from config.config import *

#generate a label.txt from all the images under a given folder
#path: /home/lokhiufung/PaddleOCR/train_data/tra-chinese; mode:train/val/test


def label(data_path,mode):
    folder = os.path.join(data_path, mode)  
    labelname ='rec_gt_'+ mode+ '.txt'
    save = os.path.join(data_path, labelname)  # /home/lokhiufung/PaddleOCR/train_data/tra-chinese/rec_gt_train.txt
    with open(save,'w') as txt: # 打开标签文件准备写入


       for img in os.listdir(folder):  # image name
           cha = img.split('.')[0][0]
           label=os.path.join(mode,  img) + '\t' + cha + '\n' #eg.   train/1.png  用
            
           txt.write(label)  # 写入文件

    txt.close()  
        

def divide(image_dir, root_dir): #for us, /ocr_dara/tra-chinese/data/orig ; /paddleocr/train_data/tra-chinese
    
   random.seed(123) # give random seed 
   
   # define the ratio of train/valid/test
   train_ratio = 0.7
   valid_ratio = 0.15
   test_ratio = 0.15

# get the filename of image/txt files
   image_filenames = [f for f in os.listdir(image_dir)]
   
# randomize the file list
   random.shuffle(image_filenames)

# calculate the number of files for each classification
   total_count = len(image_filenames)
   train_count = int(total_count * train_ratio)
   valid_count = int(total_count * valid_ratio)
   test_count = total_count - train_count - valid_count

# define the output directory
   train_image_dir = os.path.join(root_dir, 'train')
   valid_image_dir = os.path.join(root_dir, 'valid')
   test_image_dir = os.path.join(root_dir, 'test')

# create the above directories
   os.makedirs(train_image_dir, exist_ok=True)
   os.makedirs(valid_image_dir, exist_ok=True)
   os.makedirs(test_image_dir, exist_ok=True)

# division
   for i, filename in enumerate(image_filenames):        
        if i < train_count:
           output_image_dir = train_image_dir
          
        elif i < train_count + valid_count:
           output_image_dir = valid_image_dir 
           
        else:
           output_image_dir = test_image_dir
                      
        # copy image files
        src_image_path = os.path.join(image_dir, filename)
        dst_image_path = os.path.join(output_image_dir, filename)
        shutil.copy(src_image_path, dst_image_path) 
     

#at the end 
if __name__ == '__main__':
    divide(TRA_CHI_IMAGE_PATH,ROOT_PATH)
    #generate the label file for each catogary
    label(ROOT_PATH,'train')
    label(ROOT_PATH,'valid')
    label(ROOT_PATH,'test')