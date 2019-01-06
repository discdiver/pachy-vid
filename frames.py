# frames.py
# code for video to image frames pachyderm example

import os
import cv2
import numpy as np
import argparse

# command line arguments
parser = argparse.ArgumentParser(description='Get params for video to images')
parser.add_argument('indir', type=str, help='Input directory containing videos')
parser.add_argument('outdir', type=str, help='Output directory for images')
parser.add_argument('max_images', type=int, help='Max frames to output per video')
args = parser.parse_args()

def make_images(video, outdir="/pfs/out", max_images=1000):
    '''
    Outputs .jpg images from a video file

    Args:
        video (str):                          File name of video
        outdir="/pfs/images_pipeline" (str):  Output directory
        max_images=1000 (int):                Max frames to output per video
    Returns:
        none
    '''

    file_name_w_ext = os.path.split(video)[1]
    file_name = file_name_w_ext.split(".")[0]  # files with . in name could trip

    vidcap = cv2.VideoCapture(video)
    vid_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    count = 0                                 # counter to stay under max images
    output_dir = f"{outdir}/{file_name}"

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)                  # cv2 requires directory to exist

    while count < max_images and count < vid_length:
        try:
            success, image = vidcap.read()
            cv2.imwrite(
                os.path.join(
                    output_dir,
                    file_name + "frame{:d}.jpg".format(count)),
                    image
                )
        except Exception as e:
            print("Oops, there was an exception: {}".format(e))

        count += 1

# walk /pfs/<input_repo> and call make_images on every file
for dirpath, dirs, files in os.walk(args.indir):
    for file in files:
        make_images(os.path.join(dirpath, file), args.outdir, args.max_images)
