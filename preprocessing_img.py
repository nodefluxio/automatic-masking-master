import cv2 
import glob
import os
from PIL import Image
import dlib
import numpy as np

def resize_and_save(path, path_tmp, out_h_size):
    path = 'data/raw2'
    path_out = path_tmp
    out_h_size = 720
    images = os.listdir(path)
    try:
        os.mkdir(path_out)
    except:
        print('folder was created')
    # read image
    for filename in images:
        filename_in = path + '/' + filename
        img = Image.open(filename_in)

        # resize
        h, w = img.size
        img_ratio = w/h
        resize = (out_h_size, int(out_h_size*img_ratio))
        img = img.resize(resize)

        filename_out = filename.split('.')[0] + '.jpg'
        output_filename = path_out + '/' + filename_out
        
        img = img.convert('RGB')
        img.save(output_filename)
        print('Success resize image. Ouput: ', filename_out) 
    # for filename in images:      

def face_rotate(path_tmp, path_out):
    path = path_tmp
    images = os.listdir(path_tmp)
    detector = dlib.get_frontal_face_detector()
    arr_rotate = [0, 90, 180, 270]
    try:
        os.mkdir(path_out)
    except:
        print('folder was created')
    # read image
    for filename in images:
        filename_in = path + '/' + filename
        img = Image.open(filename_in)

        filename_out = filename.split('.')[0] + '.jpg'
        output_filename = path_out + '/' + filename_out
        
        img = img.convert('RGB')
        # print(img.getexif())
        
        for angle in arr_rotate:
            img = img.rotate(angle, expand=1)
            np_img = np.array(img)
            bbox = detector(np_img, 1)
            if len(bbox) > 0:
                print("Angle orientation: ", angle)
                break 
        print(bbox)
        if len(bbox) == 0:
            img = img.rotate(0, expand=1)
            print('No Face Detected')
        img.save(output_filename)
        print('Success rotate image. Ouput: ', filename_out)  


if __name__ == '__main__' :
    path = 'data/raw2'
    path_tmp = 'data/raw_tmp'
    path_out = 'data/raw_out'

    out_h_size = 720
    resize_and_save(path, path_tmp, out_h_size)
    face_rotate(path_tmp, path_out)