Clone the repo using this command:
```bash
git clone https://github.com/metalpole/rea.git
```
and `cd` into the cloned directory.

To make setup easier a Docker container will be used, so having Docker installed will be necessary. Use the following command to pull the necessary image (which I recently used) courtesy of DeepLearning.AI which already contains Jupyter lab, FastAPI and Tensorflow.

Using the following command will download the image to run this repo locally:
```bash
docker pull deeplearningai/mlepc1w1-ugl:jupyternb
```

To run a container using the image you just pulled, double check that you are currently on the cloned directory and use this command:
```bash
docker run -it --rm -p 8888:8888 -p 8000:8000 --mount type=bind,source="$(pwd)",target=/home/jovyan/work deeplearningai/mlepc1w1-ugl:jupyternb
```

Use the given token/hyperlink to open up Jupyter in your browser. Enter the `work` directory. Open the `ipynb.ipynb` notebook. Also, open a new terminal as shown.

![Alt text](terminal.png?raw=true "Title")