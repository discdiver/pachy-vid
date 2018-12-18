# Pachyderm Development Workflow

_Up and Running Local Development with Minikube_
Prerequisites: minikube and pachyderm installed (follow instructions to install here).

Step 1: Delete and start minikube machine with `minikube delete` and then `minikube start` 
Step 2: Deploy Pachyderm with `pachctl deploy local`
Step 4: Check Pachyderm pods all running with kubectl get pods.
Step 5: Port forward

Or this might be a one shot setup
set `eval $(minikube docker-env)` You can then build an image, and push it directly into minikube (no need for registry) to use as part of your pipeline.

Project building
Step 1. Set up a repo on pachyderm if you odn't have one already.
Step 1. Get your code to work locally.
Step 2. 
Step 3: Manually update your json spec to match your image tag 
Step 4: Call update-pipeline
Step 5. Change code
Step 6. Docker build new code *w/ unique tag*. With _Docker-env set, this will build the image in minikube directly_
Step 7. Update json spec
Step 8. Run pachctl update-pipeline -f new.json
