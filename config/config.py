import os

PROJECT_NAME = 'written-english'
PROJECT_PATH = os.path.realpath(os.path.join('..', PROJECT_NAME)) #open the terminal at  '/home/lokhiufung/git/AI_approval_officer'
 #project path: /home/lokhiufung/git/written-eng

ORIGINAL_PATH = os.path.join(PROJECT_PATH, 'images/')
TICK_PATH = os.path.join(PROJECT_PATH, 'ticks/')
SIGN_PATH = os.path.join(PROJECT_PATH, 'signs/')


IMAGE_PATH= os.path.join(PROJECT_PATH, 'class/by_class') # download the image under '/home/lokhiufung/written-eng'
ROOT_PATH = os.path.join('../PaddleOCR/train_data/written-eng')#path of the newly-generated folder
