Clone the repo using this command:
```bash
git clone https://github.com/metalpole/rea.git
```
and `cd` into the cloned directory.

To make setup easier a Docker container will be used, so having Docker installed will be necessary. Use the following command to pull the necessary image (which I recently used) courtesy of DeepLearning.AI which already contains Jupyter lab, FastAPI t

Using the following command will download or pull the image necessary to run this ungraded lab locally:
```bash
docker pull deeplearningai/mlepc1w1-ugl:jupyternb
```

To run a container using the image you just pulled, double check that you are currently on the cloned directory and use this command:
```bash
docker run -it --rm -p 8888:8888 -p 8000:8000 --mount type=bind,source="$(pwd)",target=/home/jovyan/work deeplearningai/mlepc1w1-ugl:jupyternb
```