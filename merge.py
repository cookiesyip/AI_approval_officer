import cv2
import matplotlib.pyplot as plt
import time
import os
from config.config import *

image_list = []
tick_list = []
sign_list = []
position_list = []

p1 = [[585,1980], [645,1980], [585,2040], [645,2040]]
p2 = [[875,1980], [935,1980], [875,2040], [935,2040]]
p3 = [[1165,1980], [1225,1980], [1165,2040], [1225,2040]]
p4 = [[1458,1980], [1518,1980], [1458,2040], [1518,2040]]
p5 = [[150,3450], [900,3450], [150,3650], [900,3650]]
position_list.append(p1)
position_list.append(p2)
position_list.append(p3)
position_list.append(p4)
position_list.append(p5)


def get_image_path(path):
    # Read and save all png documents' full path and return a list.
    all_files = []
    for p, dirname, filename in os.walk(path):
        for i in filename:
            all_files.append(os.path.join(p + i))
    return all_files

def replace_img_data(img, replace_sub_img, box):
    new_img = img.copy()

    replace_shape = new_img[box[0][1]:box[3][1], box[0][0]:box[1][0]].shape
    dim = (replace_shape[1], replace_shape[0])
    resized = cv2.resize(replace_sub_img, dim)

    new_img[box[0][1]:box[3][1], box[0][0]:box[1][0]] = resized

    return new_img

sign_list = get_image_path(SIGN_PATH)
print(sign_list[0])
'''for i in range(4):
    for k in range(27):
        plt.clf()
        plt.figure(figsize=(100,100))
        plt.imshow(replace_img_data(cv2.imread('./images/original' + str(i+1) + '.png'), cv2.imread('./ticks/' + str(k+1) + '.png'), position_list[i]))
        plt.savefig('./results/image' + str(i) + '_' + str(k) + '.png')
        plt.close('all')'''
        

for k in range(40):
    k += 1217
    plt.clf()
    plt.figure(figsize=(100,100))
    plt.imshow(replace_img_data(cv2.imread('./images/original5.png'), cv2.imread('./signs/blank.png'), [[150,3450], [900,3450], [150,3650], [900,3650]]))
    plt.savefig('./sign_results/image' + str(k) + '.png')
    plt.close('all')