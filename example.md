# Example

## Videos to image frames with Pachyderm

[]<img src="https://raw.github.com/discdiver/pachy-vid/camera.svg?sanitize=true
      
In this example you'll use Pachyderm to take one or more video files and split them into individual frames using the cv2 library. Although it requires little code, this program is pretty cool. With this example running, getting individual frames from videos is a piece of cake. 

Pachyderm quickly processes multiple videos simultaneously through parallelization. Additionally, when videos are added, the pipeline runs automatically, outputting nicely organized frames for your videos. Then you'll have pictures you can put on coffee mugs and calendars.

 Let's get started!

## Prerequisites
This example assumes you have Pachyderm running locally. Check out the [Local Installation instructions](https://pachyderm.readthedocs.io/en/stable/getting_started/local_installation.html) if you haven’t istalled pachyderm. 

This example also assumes you have done the [Beginner Tutorial](https://pachyderm.readthedocs.io/en/stable/getting_started/beginner_tutorial.html). You don't have to have completed it, but this guide won't explain what's going on in the level of detail that guide does.

## Step 1: Create a Pachyderm Repo

``` pachctl create-repo videos

# list repo
pachctl list-repo
```

## Step 2: Create a Pachyderm Pipeline

Pipelines are specified with JSON. For this example, we've already created a pipeline for you. The code is here:. The full pipeline spec is here.

When you want to create your own pipelines later, you can refer to the full :doc:`../reference/pipeline_spec` to use more advanced options. This includes building your own code into a container instead of the pre-built Docker image we'll be using here.

For now, we're going to create one pipeline that takes one or more videos and outputs up to the first 1,000 frames. When a pipeline is created, Pachyderm runs your code on the data in your input repo. The pipeline runs again to process the videos for all future commits. 

This first time Pachyderm runs a pipeline, it downloads the Docker image specified in the pipeline spec from the specified Docker registry (DockerHub in this case). The first run this might take a few mintues, depending on your Internet connection speed. Subsequent runs will be much faster.

Here's the pipeline spec, python code, and Dockerfile that make the magic happen for this app.

Below is the pipeline spec and python code we're using. Let's walk through the details.

# frames.json
```
{
  "pipeline": {
    "name": "images_pipeline"
  },
  "input": {
    "atom": {
      "glob": "/*",
      "repo": "videos"
    }
  },
  "transform": {
    "cmd": [ "python", "./frames.py" ],
    "image": "discdiver/frames:v1.32"
  },
  "parallelism_spec":{
    "coefficient": 2
  },
  "enable_stats": true,
}
```

This Pachyderm pipeline spec contains five sections. First is the pipeline name, *frames*. Third is the input. Here we have one "atom" input: our images repo with a '/*' glob pattern. Second is the transform that specifies the Docker image to use, *discdiver/frames:v1.32* (defaults to Docker Hub for the registry), and the entry point script *frames.py*. 

The glob pattern defines how the input data can be broken up for parallel processing. '/*' means that each top level file can be processed individually, assuming you have enough workers available. This setting makes sense for videos in this example. Glob patterns are one of the most powerful features of Pachyderm. When you start creating your own pipelines, check out the :doc:`../reference/pipeline_spec`. 

The final part of the pipeline spec is "enable_stats:true", which allows you to see useful information about the pipeline


CHANGE this, this is just placeholder.
```
# frames.py
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

```

ython code is really straight forward. We're simply walking over all the images in /pfs/images, do our edge detection and write to /pfs/out.

/pfs/images_pipeline and /pfs/out are local directories that Pachyderm creates for you. All the input data for a pipeline will be found in */pfs/input_repo_name*, where *input_repo_name* is specified in your Pachyderm .json specification file. 

Your code should always write out to */pfs/out* or a subdirectory you create inside */pfs/out*. Pachyderm will automatically gather everything written to /pfs/out and version it as the pipeline's output commit.


## Step 3: Put Data into Pachyderm

From the command line use `put-file` along with the `-f` flag to denote a local file, a URL, or an object storage bucket (e.g. s3). In this case, if you have the current repo cloned you can just upload a video file from this project folder. Or you can upload a video file of type .mp4, .flv, mkv, or 3gp. 

Also specify the repo name "videos", the branch name "master", a name for the video file, e.g. "buck_bunny.mp4", and the path to the file.

``` pachctl put-file videos master buck_bunny.mp4 -f /buck_bunny.mp4 ```

When you add a file to Pachyderm it automatically makes a commit of your data. 

## Step 4: View the commit 
See the commit with
```pachctl list-commit videos```
and see the files committed with  
```pachctl list-file videos master```

## Step 5: View your beautiful image frames
See the individual frames by getting them from Pachyerm and viewing them with one of the following commands:
```
# on OSX
$ pachctl get-file images_pipeline master buck_bunny/buck_bunnyframe1.jpg | open -f -a /Applications/Preview.app
```

SHOW screenshot of images.

## Step 7: Explore your pipeline in the Pachyderm dashboard
When you deployed Pachyderm locally, the Pachyderm Enterprise dashboard was also deployed by default. This dashboard lets you interactively visualize, manipulate, and debug your pipeline. You can also explore your data on the dashboard. To access your dashboard visit localhost:30080 in an internet browser (e.g., Google Chrome). You should see something similar to this:
**image of dashboard**

## Step 8: Build off this example
You've seen just how easy it is to set up a Pachyderm Pipeline that takes in a file of one type, manipulates it, and ouptputs new files. To make changes to *frames.py* or *frames.json* and quickly iterate, check out the [Pachyderm Workflow]() document.

## Step 9: Try out another example or jump into the docs. 
[Pachyderm Examples](http://docs.pachyderm.io/en/stable/examples/README.html)
[Pachyderm Fundamentals](http://docs.pachyderm.io/en/stable/fundamentals/getting_data_into_pachyderm.html)

We're hear to help you every step of the way. Please submit any issues or questions you come across on GitHub, Slack, or email at support@pachyderm.io!

Icons from FlatIcon[https://www.flaticon.com/].
