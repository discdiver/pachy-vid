# pachy-vid
#Pachyderm video to frames project

# This is a draft. Do not attempt to use yet.

This repo is a Pachyderm demonstration project. The user is able to break a video file into image frames on Pachyderm using v2c. 

This repo contains three code files, this readme file, a markdown file explanation that could be part of the official examples, and a markdown file that could serve as a cookbook recipe for developing in Pachyderm. 

The three code files are the *Dockerfile*, *frames.json*, and *frames.py*. *frames.json* contains the pachyderm pipeline specification and *frames.json* contains the application code.

Additionally, this project was the impetus for the a multi-part Medium series on Docker. The first part of that series is available here. 

In this readme I'll first explain how to run the code and then explain the design decisions I made during the project. 

# Running the code locally

Step 1: Start pachyderm (see here for install and getting started).
Step 2: Clone or copy paste or pull docker file?
Step 3: Start 
Step 4: Upload a video of your choosing in the format of your choosing. Ocassionally there can be wierd codecs issues. For a video that works, try the classic available here. - or just mp4. 
Step 5: Check your X folders for output


Notes: 
1. As this is a demonstration project and we don't want resource use to get out of control, this program outputs a maximum of 1,000 frames per video. If a video has less than 1,000 frames, then all frames in the video will be output.
2. You can upload multiple videos for simultanteous processing.
3. Every time you upload a video the Pachyderm pipeline will be triggered to run automatically.


**May add ability to pass parameters for how many frames to output - would need to keep it under a certain limit


## Design decision narrative

In the code I used an updated version of cv2, a popular image and video processing library in Python to convert the video file into individual images.

I decided to output each video's frames to a labeled directory. I labeled each frame file with the name of the video it origiginated from and the frame number.

### Dockerfile:
- Used the Pachyderm beginner tutorial Dockerfile as a starting point and reworked it following several best practices. 
- Updated the parent Ubuntu image to the latest version.
- Had to add a timezone package and install it earlier than some other packages to remove a prompt that made the Dockerfile build fail.
- Moved opencv install to a pip3 install
- Put one package to install on each line for legibility.
- Removed the unneeded numpy package.
- Removed the clean command because I read that Ubuntu image does that automatically after build.

### .py file
- Created a function to turn videos into images.
- Function finds number of frames in video
- Function outputs total number of frames up to a maximum of 1,000.
TODO - User can input number of frames to output up to a max of 1,000.
- Wraps the read and write in a try-except statement for error catching
- Each video's image frames are written to a directory with name of the video
- Each frame is identified by the video's prefix and a number (i.e. frame one has the number 1).

The code walks the file system to find all videos and calls make_images() for each video.
