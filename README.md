# Pachyderm Video to Image Project

![Screenshot](images/ssread.png)

This repo contains a Pachyderm demonstration project. It shows how a user can easily break a video file into image frames using [Pachyderm](http://pachyderm.io/) and the [opencv library](https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html). 

This repo contains the following files of consequence:
- *README.md* - this file.
- *example.md* - An example file similar to other examples in the Pachyderm docs.
- A *Dockerfile* 
- *frames.json* with the pachyderm pipeline specification 
- *frames.py* contains the application code.
- Sample video files in several formats.
- *FAQ.md* a draft FAQ with answers that could be helpful for new Pachyderm users. 
- *workflow.md* -  A draft document that could potentially be used as a cookbook recipe for new Pachyderm users to quickly learn a development workflow. 

In this readme I'll first explain how to run the code and then explain the design decisions I made during the project. 

# Running the code locally
1. Start pachyderm.
2. Make a repo named `videos`.
3. Make a pipeline using the `frames.json` file in this repo.
4. Upload a video in one of the following formats: .mp4, .flv, mkv, or 3gp. into your videos repo. Occasionally with videos, I understand there can be weird codecs issues. For sample videos without codecs issues, try the ones in this repo taken from [sample_videos.com](https://sample-videos.com/index.php#sample-mp4-video).
5. You can retrieve the image files from their subfolders. Alternatively, in the Pachyderm dashboard you'll see the video files come in and the .jpg image files go into their respective folders. You can click on the images and view them or download them.

### Notes
1. This program outputs a maximum of frames per video that can be set by the user in frames.json. If a video has less than the number of frames, then all frames in the video are output. 
2. You can upload multiple videos for simultaneous processing.
3. Each time you upload a video the Pachyderm pipeline will be triggered to run automatically.

# Design decisions and explanation
In the code I used an updated version of opencv, a popular image and video processing library in Python, to convert the video files into individual images.

I decided to output each video's frames to a labeled directory to demonstrate that subfolders can be easily created in Pachyderm. I labeled each image file with the name of the video it originated from and the frame number for a nice user experience.

### Dockerfile
The Dockerfile uses an image with Python and opencv. 

### frames.py
This is the main application file. I created a *make_images()* function to turn videos into images. The parameter *max_images* is easily altered in the .json file if a different number is desired.

The function finds the total number of frames in video. The read and write functions are wrapped in a try-except block. Each video's frames, up to *max_images* are written to a file in a sub-directory with the name of the video. Each image file is identified by the video's prefix and the frame number. 

This script walks the file system to find files that match the specified video formats and calls *make_images()* for each file.

### frames.json
This is the Pachyderm pipeline specification. It pulls the Docker image from my Docker Hub registry. The *parallelism_spec* is set to *constant: 2* to use 2 workers and the *glob* pattern specifies Pachyderm should run each top level file or directory in the input repo as its own datum. This arrangement should make for efficient parallel processing of multiple video files.

The transform command contains the input repository, output repository, and max_images.

### example.md
This file is a walkthrough of the project for someone new to Pachyderm. It exposes the tutorial user to the Pachyderm dashboard and aims to provide helpful, clear explanations. 

### FAQ.md
The FAQ file is a work in progress. I thought I'd share some Pachyderm questions that came to mind during this project that might be useful for new users. I also included some questions from the Users Slack channel that look like they could be helpful for folks.

### workflow.md
New users who want to quickly iterate with Pachyderm might find this brief workflow document helpful. I've shared it with the Pachyderm Users Slack channel in the expectation that other users and the Pachyderm team might have tweaks to it and now it's being collaboratively developed as a [Google Doc](https://docs.google.com/document/d/1a2QkXG9y81VFqAswOeSzBROrys5XHK1YSJk6xfUja2A/edit?usp=sharing).
