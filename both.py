import base64
import os
import random
import shutil
import tra_chinese
import written_eng
from config.config import *

def label(root_dir,mode):
    folder= os.path.join(ROOT_PATH,mode)
    labelname ='rec_gt_'+mode+'.txt'
    save = os.path.join(ROOT_PATH, labelname)  # /home/lokhiufung/PaddleOCR/both/rec_gt_train.txt
    with open(save,'w') as txt: 
        for img in os.listdir(folder):
            if img[1]=='_': #it is a traditional chinese character
                cha = img.split('.')[0][0]
                label=os.path.join('train',  img) + '\t' + cha + '\n' #eg.   train/1.png  用
                txt.write(label)        
   
            else: 
                cha = img.split('_')[1]
                label=os.path.join('train',  img) + '\t' + str(base64.b16decode(cha.upper()).decode()) + '\n' #eg. train/4a_/...;.png  K
                txt.write(label)  

    txt.close()


if __name__=='__main__':

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
    label(ROOT_PATH,'train')
    label(ROOT_PATH, 'test')
