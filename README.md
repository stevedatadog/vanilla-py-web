Vanilla Python Web Server
===

This is a Docker image for testing a simple HTTP web server in a 
containerized environment. Aside from python3, it has no dependencies.

`app/app.py` is the script for the web server.

`.github/workflows/deploy-image.yaml` automatically builds the Docker image 
with each commit to `main`, and pushes it to GHCR.

`deploy/` contains manifests for deploying the app as a pod or deployment, and
service.


