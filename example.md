# Example
# DRAFT. DO NOT USE.
## Videos to Frames

##Insert video camera, flipped arrow, still camera and pachyderm logo

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
REPLACE
{
  "pipeline": {
    "name": "edges"
  },
  "transform": {
    "cmd": [ "python3", "/edges.py" ],
    "image": "pachyderm/opencv"
  },
  "input": {
    "atom": {
      "repo": "images",
      "glob": "/*"
    }
  }
}
```
Our pipeline spec contains four simple sections. First is the pipeline name, frames. Second is the transform that specifies the Docker image to use, pachyderm/frames (defaults to DockerHub for the registry), and the entry point frames.py. Third is the input. Here we have one "atom" input: our images repo with a '/*' glob pattern.

The glob pattern defines how the input data can be broken up for parallel processing. '/*' means that each top level file can be processed individually, assuming you have enough workers available. This setting makes sense for videos and the file structure we've defined. Glob patterns are one of the most powerful features of Pachyderm. When you start creating your own pipelines, check out the :doc:`../reference/pipeline_spec`. 

The final part of the pipeline spec is "enable_stats", which allows you to see useful information about the pipeline ??


CHANGE this, this is just placeholder.
```
# frames.py
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# make_edges reads an image from /pfs/images and outputs the result of running
# edge detection on that image to /pfs/out. Note that /pfs/images and
# /pfs/out are special directories that Pachyderm injects into the container.
def make_edges(image):
   img = cv2.imread(image)
   tail = os.path.split(image)[1]
   edges = cv2.Canny(img,100,200)
   plt.imsave(os.path.join("/pfs/out", os.path.splitext(tail)[0]+'.png'), edges, cmap = 'gray')

# walk /pfs/images and call make_edges on every file found
for dirpath, dirs, files in os.walk("/pfs/images"):
   for file in files:
       make_edges(os.path.join(dirpath, file))
```

Our python code is really straight forward. We're simply walking over all the images in /pfs/images, do our edge detection and write to /pfs/out.

/pfs/images and /pfs/out are special local directories that Pachyderm creates within the container for you. All the input data for a pipeline will be found in /pfs/<input_repo_name> and your code should always write out to /pfs/out. Pachyderm will automatically gather everything you write to /pfs/out and version it as this pipeline's output.



## Step 3: Put Data into Pachyderm

From the command line use ` put-file` along with the `-f` flag to denote a local file, a URL, or an object storage bucket. In this case, if you have the current repo cloned you can just upload the video file in this project folder. Or you can upload other video files.

Also specify the repo name "videos", the branch name "master", and what we want to name the video file, "buck_bunny.png".

``` pachctl put-file videos master buck_bunny.mp4 -f /buck_bunny.mp4 ```

When you add file to Pachyderm it make a commit, much like a Git commit. 

## Step 4: View the commit 
See the commit with
```pachctl list-commit videos```
and see the files committed with  
```pachctl list-file videos master```

## Step 5: View your beautiful image frames
See the individual frames by getting them from Pachyerm and viewing them with one of the following commands:
```
# on OSX
$ pachctl get-file videos master buck_bunny01.png | open -f -a /Applications/Preview.app

# on Linux
$ pachctl get-file videos master buck_bunny0001.png | display
```

SHOW screenshot of images.

Step 7: Explore your pipeline in the Pachyderm dashboard
When you deployed Pachyderm locally, the Pachyderm Enterprise dashboard was also deployed by default. This dashboard lets you interactively visualize, manipulate, and debug your pipeline. You can also explore your data on the dashboard. To access your dashboard visit localhost:30080 in an internet browser (e.g., Google Chrome). You should see something similar to this:
**image of dashboard**

Step 8: Build off this example
You've seen just how easy it is to set up a Pachyderm Pipeline that takes in a file of one type, manipulates it, and ouptputs new files. 

Step 9: Try out another example or jump into the docs. LINKS


We're hear to help you every step of the way. Please submit any issues or questions you come across on GitHub, Slack, or email at support@pachyderm.io! LINKS


