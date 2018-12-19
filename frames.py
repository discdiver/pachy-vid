# frames.py
# code for video to image frames pachyderm example

import os
import cv2
import numpy as np

top = os.getcwd()

print('hello')

def make_images(video):
    '''
    Output an image for each of first 1000 frames in each video

    Args:
        video: string  # file name of video
    Returns:
        none
    '''

    file_name = os.path.split(video)[1]
    file_no_ext = file_name.split(".")[0]   # watch out for . in file name

    vidcap = cv2.VideoCapture(video)
    vid_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    count = 0
    #print("/pfs/out/{}".format(file_no_ext))
    # os.mkdir("/pfs/out/{}".format(file_no_ext))  #cv2 requires directory to exist to write to it

    while count < 1000 and count < vid_length:
        try:
            success, image = vidcap.read()
            cv2.imwrite(os.path.join("/pfs/out", file_no_ext+"frame{:d}.jpg".format(count)), image)
            # TESTING LOCALLY
            # cv2.imwrite(video+"frame{:d}.jpg".format(count), image)
        except Exception as e:
            print("Oops, there was an exception: {}".format(e))

        count += 1

# walk /pfs/videos and call make_images on every file found
for dirpath, dirs, files in os.walk("/pfs/videos"):
    for file in files:
        if file[-3:] == 'mp4':  # change to in vidtypes and define set vidtypes
            make_images(os.path.join(dirpath, file))
