# Singularity Kernel Install

A tool for installing Singularity containers as separate Jupyter kernels, allowing easy switching between different isolated environments.

## TLDR

```bash
singularity-kernel-install /path/to/myimage.sif
```

Then, e.g. in JupyterLab reload the browser and select the `myimage` kernel from the menu.

## Requirements

Dependencies:
- [Jupyter](https://jupyter.org/install) (notebook or lab)
- Python 3.6+
- For R kernels: R with IRkernel installed in the container

## Installation

### Install from GitHub

In just one command:

```bash
pip install git+ssh://git@github.com/JPatrickPett/singularity_kernel_install.git
```

Or by cloning the repository:

```bash
# Clone the repository
git clone https://github.com/JPatrickPett/singularity_kernel_install.git
cd singularity_kernel_install

# Install the package
pip install -e .
```

This will install the `singularity-kernel-install` command globally.

## Usage

### Basic Usage

```bash
# Install as Python kernel (default)
singularity-kernel-install /path/to/your-container.sif

# Install as R kernel
singularity-kernel-install /path/to/your-container.sif --language r
```

This will register a new Jupyter kernel using the container's filename as the kernel name.

### Advanced Options

```bash
# Python kernel with custom options
singularity-kernel-install /path/to/your-container.sif \
    --name "my-kernel" \
    --display-name "My Custom Python Kernel" \
    --python-path "/opt/conda/bin/python"

# R kernel with custom options
singularity-kernel-install /path/to/your-container.sif \
    --language r \
    --name "my-r-kernel" \
    --display-name "My Custom R Kernel" \
    --r-path "/usr/local/bin/R"
```

Options:
- `--language` or `-l`: Kernel language (choices: "python", "r", default: "python")
- `--name` or `-n`: Set a custom kernel name (default: container filename)
- `--display-name` or `-d`: Set a custom kernel display name in Jupyter
- `--python-path` or `-p`: Set the path to Python executable inside the container (default: "python")
- `--r-path` or `-r`: Set the path to R executable inside the container (default: "R")

## Creating Compatible Singularity Images

### For Python Kernels
Your Singularity container must have:
1. Python installed
2. The `ipykernel` package installed

### For R Kernels
Your Singularity container must have:
1. R installed
2. The `IRkernel` package installed

### Example Using Docker for Python

1. Create a Dockerfile:

```dockerfile
FROM python:3.9-slim

# Install Jupyter dependencies
RUN pip install --no-cache-dir jupyter ipykernel

# Optional: Install additional packages
RUN pip install --no-cache-dir numpy pandas matplotlib scikit-learn

# Optional: Set a working directory
WORKDIR /work
```

### Example Using Docker for R

1. Create a Dockerfile:

```dockerfile
FROM rocker/tidyverse:latest

# Install IRkernel
RUN R -e "install.packages(c('IRkernel'), repos='https://cran.rstudio.com/')"
RUN R -e "IRkernel::installspec(user = FALSE)"

# Optional: Install additional R packages
RUN R -e "install.packages(c('dplyr', 'ggplot2'), repos='https://cran.rstudio.com/')"

# Optional: Set a working directory
WORKDIR /work
```

2. Build the Docker image:

```bash
docker build -t jupyter-r-container .
```

3. Convert to Singularity image:

```bash
singularity build jupyter-r-container.sif docker-daemon://jupyter-r-container:latest
```

## Troubleshooting

### Kernel Connection Issues

If the kernel fails to connect:
- Ensure Singularity has proper permissions
- Check if Python/R path is correct inside the container
- Verify ipykernel (Python) or IRkernel (R) is installed in the container

### Testing Your Container

To test if your container can run as a kernel:

```bash
# For Python kernels
singularity exec your-container.sif python -c "import ipykernel; print('ipykernel is installed')"

# For R kernels
singularity exec your-container.sif R -e "if('IRkernel' %in% installed.packages()[,'Package']) print('IRkernel is installed') else print('IRkernel is NOT installed')"
```
