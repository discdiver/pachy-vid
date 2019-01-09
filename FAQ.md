# Pachyderm FAQ

### Using Pachyderm locally with minikube, what do I do if I need to restart? 

`minikube delete`, `minikube start`, `pachctl deploy local`, port forward. See suggested workflow [here]().

### How long does Pachyderm take to to get my k8s pods running?

It can take five minutes or so with minikube, and is generally much faster with Docker Desktop.

### How long does port forwarding take?

If it hasn't completed in a few minutes, try `export ADDRESS=<minikubeIP>:30650`.

### Can I start processing one job before another finishes?

Nope. Jobs get processed one at a time because often times the execution of one job depends on the previous job's result.

### What's the best way to commit large files to Pachyderm from my local machine?

`export ADDRESS=<minikubeIP>:30650` instead of port-forward. 

### What's the best way to commit large files from an S3 bucket?

`put-file repo master -f s3://...` 

### After uploading data to a repo that outputs data via a pipeline to a pipeline repo, the list-repo command show the size of the output repo still at 0B. Does this mean I don't have any data in the output repo?

Not necessarily. This is a bug and a fix is in the works. Use `pachctl list-commit my_output_repo_name` to see if any files were output.

### Can I use Pachyderm locally with a Windows machine?

Yes, see the installation [instructions](http://docs.pachyderm.io/en/stable/getting_started/local_installation.html).

### How can I figure out why my job failed?

Run `pachctl inspect-job my_job_id` and it will give you a `reason` field.

### How can I save pipeline definitions created in a supported Pachyderm language client into a JSON file?

`extract-pipeline`

### For a machine learning workflow, if I want to outpout both transformed data (e.g. images) and hyperparameters learned during training, how should I set that up? 

Output the images and hyperparameters into two different directories in the same output repo. Matching results/configs are stored in the same commit, so the process is easy to reason about. Then have a downstream pipeline use a glob pattern such as `/config/*` to only consume the hyperparameters and not the other output files.

### How should I back up my Pachyderm stuff?

`pachctl extract` It can back up the following, if you include your object store:  objects, tags, repos, input commits, input branches, and pipelines. Any output data is recomputed after `pachctl restore`.  It restores the full commit structure of input repos, but in only restores the head commit of output branches. It doesn’t yet backup the enterprise key or access controls (Jan 2019).  We hope to address that in a future release. 

### How can I delete Pachyderm stuff I don't need?
Choose from the following:
```
delete-repo my_repo
delete-commit my_commit
delete-branch my_branch
delete-file my_file
delete-job my_job
delete-pipeline my_pipeline
delete-all 
```


## Kubernetes-related questions

### What's Kubernetes?

[Kubernetes](https://kubernetes.io/), a.k.a. k8s, orchestrates containers. It's an open-source system for automating deployment, scaling, and management of containerized applications.

### What's kubectl?

[kubctl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is Kubernetes's command-line tool. If you're using it with Pachyderm you'll mostly use it to inspect cluster resources.

### How should I use Pachyderm locally on a Mac?

We recommend you install [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop). See the [Pachyderm install docs](https://pachyderm.readthedocs.io/en/stable/getting_started/local_installation.html) for more info.

### What's minikube?

Minikube is a tool that runs Kubernetes locally. Minikube creates a single-node Kubernetes cluster inside a VM. It's slower and requires more configuration than Docker Desktop or MicroK8s, so it isn't our recommended solution for using Pachyderm locally.

### Minikube isn't cooperating when I try to start it, what should I do?

minikube v.0.31.0 doesn't work well with virtualbox. Fixes are forthcoming by the Kubernetes team. For now, if using VirtualBox with minikube we recommend you install minikube v0.30.0. Instructions from [minikube](https://github.com/kubernetes/minikube/releases):

On Mac OsX:

`curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.30.0/minikube-darwin-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube`

On Linux:

`curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.30.0/minikube-linux-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube`

### Can I use [microk8s](https://microk8s.io/) instead of minikube? 

Pachyderm users have reported successfully deploying Pachyderm with microk8s on Ubuntu machines. On a Mac, it's easier to use Docker Desktop.


Answers compiled from [Slack](https://pachyderm-users.slack.com/), [docs](http://docs.pachyderm.io/en/latest/), and experience.
