# Singularity Kernel Install

A tool for installing Singularity containers as Jupyter kernels, allowing you to run Jupyter notebooks inside isolated container environments.

## TLDR

```bash
singularity-kernel-install /path/to/myimage.sif
```

Then, e.g. in JupyterLab reload the browser and select the `myimage` kernel from the menu.

## Requirements

Dependencies:
- [Jupyter](https://jupyter.org/install) (notebook or lab)
- Python 3.6+

Not required for this package, but to use the kernel you will need:
- [Singularity/Apptainer](https://apptainer.org/docs/admin/main/installation.html) (3.0+)

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
singularity-kernel-install /path/to/your-container.sif
```

This will register a new Jupyter kernel using the container's filename as the kernel name.

### Advanced Options

```bash
singularity-kernel-install /path/to/your-container.sif \
    --name "my-kernel" \
    --display-name "My Custom Kernel" \
    --python-path "/opt/conda/bin/python"
```

Options:
- `--name` or `-n`: Set a custom kernel name (default: container filename)
- `--display-name` or `-d`: Set a custom kernel display name in Jupyter
- `--python-path` or `-p`: Set the path to Python executable inside the container (default: "python")

## Creating Compatible Singularity Images

Your Singularity container must have:
1. Python installed
2. The `ipykernel` package installed

### Example Using Docker

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

2. Build the Docker image:

```bash
docker build -t jupyter-container .
```

3. Convert to Singularity image:

```bash
singularity build jupyter-container.sif docker-daemon://jupyter-container:latest
```

## Troubleshooting

### Kernel Connection Issues

If the kernel fails to connect:
- Ensure Singularity has proper permissions
- Check if Python path is correct inside the container
- Verify ipykernel is installed in the container

### Testing Your Container

To test if your container can run as a kernel:

```bash
singularity exec your-container.sif python -c "import ipykernel; print('ipykernel is installed')"
```
