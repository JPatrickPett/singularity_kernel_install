from setuptools import setup, find_packages

setup(
    name="singularity_kernel_install",
    version="0.1.0",
    description="Install Singularity containers as Jupyter kernels",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/singularity_kernel_install",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "jupyter",
    ],
    entry_points={
        "console_scripts": [
            "singularity-kernel-install=singularity_kernel_install.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Jupyter",
    ],
)
