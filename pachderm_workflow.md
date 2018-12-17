# Pachyderm Development Workflow

This is a draft section of the docs for folks wondering how to most efficiently develop with Pachyderm. The answer is largely taken from a Slack channel answer from Joey Zwicker.

Save massive amounts of time by quickly iterating through development with Pachyderm. 

Step 1. Get your code to work locally.
Step 2. set `eval $(minikube docker-env)` I think
That’ll mean that you can build an image, and push it directly into minikube (no need for registry) to use as part of your pipeline.
Step 3: Manually update your json spec to match your image tag 
Step 4: Call update-pipeline
Step 5. Change code
Step 6. Docker build new code *w/ unique tag*. With _Docker-env set, this will build the image in minikube directly_
Step 7. Update json spec
Step 8. Run pachctl update-pipeline -f new.json
