# Pachyderm Development Workflow

_Up and Running Local Development with Minikube_
Prerequisites: minikube and pachyderm installed (follow instructions to install here).

Step 1: Delete and start minikube machine with `minikube delete` and then `minikube start` 
Step 2: Deploy Pachyderm with `pachctl deploy local`
Step 4: Check Pachyderm pods all running with kubectl get pods.
Step 5: Port forward

Set `eval $(minikube docker-env)` Then you can then build an image, and push it directly into minikube (no need for registry) to use as part of your pipeline.

Project building
Step 1. Set up a repo on pachyderm if you don't have one already.

Step 2. Get your code to work locally.


Step 3: Manually update your json spec to match your image tag 
Step 4: Run pachctl update-pipeline -f new.json
Step 5. Change code
Step 6. Docker build new code *w/ unique tag*. With _Docker-env_ set, this will build the image in minikube directly
Step 7. Update json spec
Step 8. Run pachctl update-pipeline -f new.json
Step 9. Check that pipeline ran
Step 10: Update code and rebuild Docker image with updated code

Back to Step 3.
