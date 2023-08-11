import os

PROJECT_NAME = 'written-english'
PROJECT_PATH = os.path.realpath(os.path.join('..',PROJECT_NAME)) #open the terminal at  '/home/lokhiufung/git/ai-...'

 #project path: /home/lokhiufung/git/written-eng

ORIGINAL_PATH = os.path.join(PROJECT_PATH, 'images/')
TICK_PATH = os.path.join(PROJECT_PATH, 'ticks/')
SIGN_PATH = os.path.join(PROJECT_PATH, 'signs/')


ENG_IMAGE_PATH = os.path.join(PROJECT_PATH, 'class/by_class') # download the image under '/home/lokhiufung/git/written-eng'
TRA_CHI_IMAGE_PATH = os.path.join(PROJECT_PATH, '../Traditional-Chinese-Handwriting-Dataset/orig')
ROOT_PATH = os.path.join(PROJECT_PATH, '../PaddleOCR/train_data/both')#path of the newly-generated folder

