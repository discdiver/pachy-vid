## What's the best way to commit large files from my local machine?

`export ADDRESS=<minikubeIP>:30650` instead of port-forward. 

## What's the best way to commit large files from an S3 bucket?

`put-file repo master -f s3://...` 

## Using Pachyderm locally with minikube, what do I do if my vm disconnects? 

minikube delete, minikube start, pachctl deploy local, port forward. See suggested workflow [here]().

## How long does Pachyderm take to to get my k8s pods running?

It can take five minutes or so.

## How long does port forwarding take?

If it hasn't completed in a few minutes, try `export ADDRESS=<minikubeIP>:30650`.

## Can I start processing one job before another finishes?

Nope. Jobs get processed one at a time because often times the execution of one job depends on the previous job's result.

## After uploading data to a repo that outouts data via a pipeline to a pipeline repo, why does the list-repo command show the size of the pipeline repo still at 0B? 

Seems like a possible bug. Use pachctl list-commit my_output_repo to see if any new files were output.

## How can I tell if Pachyderm is using my new Docker image?


## Can I use Pachyderm locally with a Windows machine?

Yes, see the installation [instructions](http://docs.pachyderm.io/en/stable/getting_started/local_installation.html).

## How can I figure out why my job failed?

Run `inspect-job my_job_name` and it will give you a `reason` field.


# Kubernetes-related questions

## What's Kubernetes?

[Kubernetes](https://kubernetes.io/), a.k.a. k8s, orchestrates containers. It's an open-source system for automating deployment, scaling, and management of containerized applications.

## What's kubectl?

[kubctl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is Kubernetes's command-line tool. If you're using it with Pachyderm you'll mostly use it to inspect cluster resources.


## What is minikube?

Minikube is a tool that runs Kubernetes locally. Minikube creates a single-node Kubernetes cluster inside a VM.

## Can I use [microk8s](https://microk8s.io/) instead of minikube? 

Pachyderm users have reported deploying Pachyderm with microk8s. Look for more information from Pachyderm on how to set microk8s up soon. Sign up for our mailing list to hear about that and other new features.

## Minikube isn't cooperating, what should I do?

minikube v.31 doesn't work well with virtualbox. Fixes are forthcoming by the Kubernetes team. For now, if using VirtualBox we recommend you install minikube v0.30.0. From [minikube](https://github.com/kubernetes/minikube/releases): 

On Mac OsX:

`curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.30.0/minikube-darwin-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube`

On Linux:

`curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.30.0/minikube-linux-amd64 && chmod +x minikube && sudo cp minikube /usr/local/bin/ && rm minikube`

If you aren't using v0.31.0 and you're having issues you can try running "rm -rf $HOME/.minikube" and then running "minikube start --vm-driver=virtualbox"
