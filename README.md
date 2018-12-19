# pachy-vid
#Pachyderm video to image frames project

This repo contains a Pachyderm demonstration project. It shows how a user can use Pachyderm to easily break a video file into image frames using [Pachyderm](http://pachyderm.io/) and the [opencv library](https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html). 

This repo contains the following files of consequence:
- *README.md* - this file.
- *example.md* - An example file similar to other examples in the Pachyderm docs.
- *workflow.md* -  A draft document that could potentially be used as a cookbook recipe for new Pachyderm users to quickly learn a development workflow. 
- A *Dockerfile* 
- *frames.json* with the pachyderm pipeline specification 
- *frames.py* contains the application code.
- Sample video files in several formats.

In this readme I'll first explain how to run the code and then explain the design decisions I made during the project. 

# Running the code locally

1. Start pachyderm.
2. Make a repo named `videos`.
3. Make a pipeline using the `frames.json` file in this repo.
4. Upload a video  in one of the following formats: .mp4, .flv, mkv, or 3gp. into your videos repo. Ocassionally with videos, I understand there can be weird codecs issues. For sample videos without codecs issues, try the ones in this repo or at [sample_videos.com](https://sample-videos.com/index.php#sample-mp4-video).
5. In the Pachyderm dashboard you'll see the video files come in and the .jpg image files go into their respective folders. You can click on the images and view them or download them.

## Notes: 
1. This program outputs a maximum of 1,000 frames per video. If a video has less than 1,000 frames, then all frames in the video are output. 
2. You can upload multiple videos for simultanteous processing.
3. Each time you upload a video the Pachyderm pipeline will be triggered to run automatically.

## Design decision narrative

In the code I used an updated version of opencv, a popular image and video processing library in Python, to convert the video files into individual images.

I decided to output each video's frames to a labeled directory. I labeled each frame file with the name of the video it origiginated from and the frame number.

As we don't want resource use to get out of control, this program outputs a maximum of 1,000 frames per video. If a video has less than 1,000 frames, then all frames in the video are output. 

### Dockerfile:
The final Dockerfile pulls from a Python opencv file with clear packages. This design keeps the Dockerfile clean.

### frames.py file
I created a function make_images() to turn videos into images. The parameter *max_images* defaults to 1,000, but that can be easily altered in the code if a different number is desired.

The Function finds the total number of frames in video. The read and write functions are wrapped in a try-except block. Each video's frames, up to *max_images* are written to a file in a sub-directory with the name of the video. Each image file is identified by the video's prefix and a the frame number. 

The script walks the file system to find files that match the specified video formats and calls *make_images()* for each file.
