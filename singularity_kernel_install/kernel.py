import json
import os
import sys
import subprocess
from pathlib import Path


def install_singularity_kernel(
    image_path, kernel_name=None, display_name=None, python_path=None
):
    """Install a Singularity container as a Jupyter kernel."""
    if not os.path.exists(image_path):
        print(f"Error: Singularity image not found: {image_path}", file=sys.stderr)
        return 1

    # Use the image filename (without extension) as the kernel name if not provided
    if not kernel_name:
        kernel_name = os.path.splitext(os.path.basename(image_path))[0]

    # Use kernel name as display name if not provided
    if not display_name:
        display_name = f"Singularity: {kernel_name}"

    # Default python path in the container
    if not python_path:
        python_path = "python"

    # Create the kernel specification
    kernel_spec = {
        "argv": [
            "singularity",
            "exec",
            "--bind",
            "{connection_file}:/connection-spec",
            image_path,
            python_path,
            "-m",
            "ipykernel_launcher",
            "-f",
            "/connection-spec",
        ],
        "display_name": display_name,
        "language": "python",
    }

    # Get the jupyter data directory
    jupyter_data_dir = (
        subprocess.check_output(["jupyter", "--data-dir"]).decode("utf-8").strip()
    )
    kernel_dir = os.path.join(jupyter_data_dir, "kernels", kernel_name)

    # Create the kernel directory if it doesn't exist
    os.makedirs(kernel_dir, exist_ok=True)

    # Write the kernel.json file
    kernel_json_path = os.path.join(kernel_dir, "kernel.json")
    with open(kernel_json_path, "w") as f:
        json.dump(kernel_spec, f, indent=2)

    print(f"Singularity kernel '{display_name}' installed successfully!")
    print(f"Kernel specification file: {kernel_json_path}")
    return 0
