# Pachyderm Development Workflow

_Up and Running Local Development with Minikube_
Prerequisites: minikube and pachyderm installed (follow instructions to install here).

1. Delete and start minikube machine with `minikube delete` and then `minikube start` 
2. Deploy Pachyderm with `pachctl deploy local`
3. Check Pachyderm pods all running with kubectl get pods.
4. Port forward (NOTE: There is an Issue/PR trying to auto-port-forward, so this can hopefully be removed soon).

Set `eval $(minikube docker-env)` Then you can then build an image, and push it directly into minikube (no need for registry) to use as part of your pipeline.

Project Building
1. Set up a repo on pachyderm if you don't have one already.
2. Get your code to work locally.
3. Manually update your json spec to match your image tag 
4. Run pachctl update-pipeline -f new.json
5. Change code
6. Docker build new code *w/ unique tag*. With _Docker-env_ set, this will build the image in minikube directly
7. Update json spec
8. Run pachctl update-pipeline -f new.json
9. Check that pipeline ran
10: Update code and rebuild Docker image with updated code

Back to Project Building Step 3.
