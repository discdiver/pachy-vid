# Pachyderm Development Workflow

This is a brief guide to help you develop with Pachyderm quickly.  

These instructions assume you are running Pachyderm on minikube, but most instructions apply for any Pachyderm development. If needed, see the [local installation instructions](http://docs.pachyderm.io/en/stable/getting_started/local_installation.html). 

## Set up Pachyderm and Port Forwarding
1. Delete and start minikube machine with `minikube delete` and then `minikube start` 
2. Deploy Pachyderm with `pachctl deploy local`
3. Check Pachyderm pods all running with `kubectl get pods`. Wait for pods to show running.
4. Port forward with your minikube ip address
```$ minikube ip
192.168.99.100
$ export ADDRESS=192.168.99.100:30650
```
5. Set `eval $(minikube docker-env)` so you can build an image and then push it directly into Pachyderm through minikube (no need to go through a registry) to use as part of your Pachyderm pipeline.

## Project Building
1. Create an input repo on Pachyderm if you don't have one already.
2. Get your code to work locally outside Docker.
3. Build a Docker image with your code and Dockerfile.
4. Get your code to work locally inside your Docker container.
5. Create a JSON pipeline spec to match your Docker image tag.
6. Run `pachctl create-pipeline -f my_pipeline_spec.json` . 

7. Update your code
8. Docker build your image with a unique tag. With _Docker-env_ set, this will build the image in minikube directly.
8. Update your json spec to reflect the new image tag (e.g. v1.1).
9. Run `pachctl update-pipeline -f my_pipeline_spec.json ----push-images' 
10. Check that pipeline ran ok.

Return to step 7 until you get everything working the way you want.

The Pachyderm team is here to help you every step of the way. Please submit any issues or questions you come across on [GitHub](), [Slack](), or email at support@pachyderm.io!
