# Pachyderm Development Workflow

_Up and Running Local Development with Minikube_
Prerequisites: minikube and pachyderm installed (follow instructions to install here).

1. Delete and start minikube machine with `minikube delete` and then `minikube start` 
2. Deploy Pachyderm with `pachctl deploy local`
3. Check Pachyderm pods all running with kubectl get pods.
4. Port forward (NOTE: There is an Issue/PR on auto-port-forwarding, so this can hopefully be removed soon).

Set `eval $(minikube docker-env)` Then you can then build an image, and push it directly into minikube (no need for registry) to use as part of your pipeline.

Project Building
1. Set up a repo on pachyderm if you don't have one already.
2. Get your code to work locally outside Docker.
3. Get your code to work locally inside a Docker container.
4. Create json pipeline spec to match your Docker image tag .
5. Run `pachctl update-pipeline -f my_pipeline_spec.json` . #Do we need to push the update here to pickup the code change? github issue also.

6. Update code to improve it.
7. Docker build new code *with a unique tag*. With _Docker-env_ set, this will build the image in minikube directly
8. Update json spec to reflect new image (e.g. v1.1).
9. Run `pachctl update-pipeline -f my_pipeline_spec.json`
10. Check that pipeline ran.

Return to step 6.
