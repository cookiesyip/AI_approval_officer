import base64
import os
import random
import shutil
import tra_chinese
import written_eng
from config.config import *


# generate the images set of the both languages together
tra_chinese.divide(TRA_CHI_IMAGE_PATH,ROOT_PATH)
for folder in os.listdir(ENG_IMAGE_PATH):   
    written_eng.divide(folder, ENG_IMAGE_PATH, ROOT_PATH)
image_filenames = [f for f in os.listdir(os.path.join(ROOT_PATH,'train'))]       
random.shuffle(image_filenames)

image_filenames = [f for f in os.listdir(os.path.join(ROOT_PATH,'test'))]       
random.shuffle(image_filenames)

#gererate the label file from the image set
#label the testing data
folder= os.path.join(ROOT_PATH,'train')
labelname ='rec_gt_train.txt'
save = os.path.join(ROOT_PATH, labelname)  # /home/lokhiufung/PaddleOCR/train_data/tra-chinese/rec_gt_train.txt
with open(save,'w') as txt: # 打开标签文件准备写入

    for img in os.listdir(folder):
        if img[1]=='_': #it is a traditional chinese character
        
            cha = img.split('.')[0][0]
            label=os.path.join('train',  img) + '\t' + cha + '\n' #eg.   train/1.png  用
            txt.write(label)  # 写入文件        

        else: 
            cha = img.split('_')[1]
            print(img,cha)
            label=os.path.join('train',  img) + '\t' + str(base64.b16decode(cha.upper()).decode()) + '\n' #eg. train/4a_/...;.png  K
            txt.write(label)  # 写入文件

txt.close()
    

 #label the testing data   
folder= os.path.join(ROOT_PATH,'test')
labelname ='rec_gt_test.txt'
save = os.path.join(ROOT_PATH, labelname)  # /home/lokhiufung/PaddleOCR/train_data/tra-chinese/rec_gt_train.txt
with open(save,'w') as txt: # 打开标签文件准备写入

    for img in os.listdir(folder):
        if img[1]=='_': #it is a traditional chinese character
        
            cha = img.split('.')[0][0]
            label=os.path.join('test',  img) + '\t' + cha + '\n' #eg.   train/1.png  用
            txt.write(label)  # 写入文件        

        else: 
            cha = img.split('_')[1]
            label=os.path.join('test',  img) + '\t' + str(base64.b16decode(cha.upper()).decode()) + '\n' #eg. train/4a_/...;.png  K
            txt.write(label)  # 写入文件

txt.close()