# How to Create Your First Docker Image and Run a Python File in a Container 🛠️ 📦

This guide will walk you through creating your first Docker image and running a Python script inside a Docker container.
we will look at 2 ways:

1. CPU-based Containers - `Dockerfile.cpu`
2. GPU-based Containers - `Dockerfile.gpu`

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your machine
- A Python script (e.g., `app.py`) in your project directory that does something (e.g., loads a Large Language Model and generates a response)

## 0. Install Docker Desktop

- Yeahhh, we need that :-)
- Create a new directory for your project so that you have structured content

```
mkdir myContainer
cd myContainer/
```

- You may have to do the formalitites of "Login/Sign in" in your docker desktop

## 1. Create a Dockerfile

#### 1.1 CPU-based

- Create a file named `Dockerfile` in your project directory with the following structure (modify them as per your need):

```dockerfile
# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Install system dependencies (only what's needed for CUDA and Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    git \

# Install all other Python dependencies with pinned versions
RUN pip install <package names with versions>

# Set the working directory in the container
WORKDIR /app

# Default command
CMD ["bash"]
```

- You can use `Dockerfile.cpu` if you want to run your container in a CPU-only Environment with manual Python setup. Ideal for testing, lightweight inference, or non-GPU machines

#### 1.2 GPU-based

- You can use `Dockerfile.gpu` if you have GPU-based Environment. This provides you with the `nvidia/pytorch:25.05-py3` NVIDIA container image (you can modify the version as per your need).

- Pre-installs PyTorch with CUDA support. Ideal for training or running models with GPU acceleration.

PS - It is a recommended practice to use a `requirements.txt` instead of installing packages directly.

## 2. Build the Docker Image

- Now we have the blueprint we need to create our first Docker image. All we have to do is BUILD THE IMAGE now so open a terminal in your project directory and run:

```
docker build -t <image_name>:version .
```

- Don't forget that DOT in the end, it specifies the directory and this is going to take some time to run...

- After the process is completed, you can check if your image is successfully created with the following command

```
docker images
```

## 3. Run a container from your Image

- Now we will create a container from your Image, which will we use to run our Python script in. Say, our dummy Image name and version is `mycontainer:v1`

```
docker run --rm -v $(pwd):/app -w /app mycontainer:v1 python test.py
```

**Command Explanation**

- `--rm`: Automatically remove the container after it exits
- `-v $(pwd):/app`: Mount the current directory to `/app` inside the container
- `-w /app`: Set `/app` as the working directory in the container
- `mycontainer:v1`: Name and tag of your Docker image
- `python test.py`: Command to run your Python script

<br />

**Congratulations! You have not only successfully created your first docker Image, but also used it to create a container and run a Python script.**

> By Piyush Pant ( पियूष पंत )
