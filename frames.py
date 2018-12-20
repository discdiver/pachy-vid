# frames.py
# code for video to image frames pachyderm example

import os
import cv2
import numpy as np

top = os.getcwd()

def make_images(video, max_images=1000):
    '''
    Outputs .jpg images from a video file

    Args:
        video (str):     File name of video
        max_images (int): Maximumum number of images to output per video.
    Returns:
        none
    '''

    file_name = os.path.split(video)[1]
    file_no_ext = file_name.split(".")[0]

    vidcap = cv2.VideoCapture(video)
    vid_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    count = 0             # counter to stay under max images
    #print("/pfs/out/{}".format(file_no_ext))
    os.mkdir("/pfs/out/{}".format(file_no_ext))  #cv2 requires directory to exist

    while count < max_images and count < vid_length:
        try:
            success, image = vidcap.read()
            cv2.imwrite(os.path.join("/pfs/out/{}".format(file_no_ext), file_no_ext + "frame{:d}.jpg".format(count)), image)
        except Exception as e:
            print("Oops, there was an exception: {}".format(e))

        count += 1

ok_file_type = {'mp4', '3gp', 'flv', 'mkv'}

# walk /pfs/videos and call make_images on every file found
for dirpath, dirs, files in os.walk("/pfs/videos"):
    for file in files:
        if file[-3:] in ok_file_type:
            make_images(os.path.join(dirpath, file))
