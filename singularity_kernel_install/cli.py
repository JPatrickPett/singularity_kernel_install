#!/usr/bin/env python3

import argparse
import sys
from .kernel import install_singularity_kernel


def main():
    """Command line interface for singularity-kernel-install."""
    parser = argparse.ArgumentParser(
        description="Install a Singularity image as a Jupyter kernel"
    )
    parser.add_argument("image_path", help="Path to the Singularity image (.sif) file")
    parser.add_argument("--name", "-n", help="Kernel name (defaults to image filename)")
    parser.add_argument("--display-name", "-d", help="Display name for the kernel")
    parser.add_argument(
        "--language",
        "-l",
        choices=["python", "r"],
        default="python",
        help="Kernel language (default: python)",
    )
    parser.add_argument(
        "--python-path",
        "-p",
        default="python",
        help="Path to Python executable inside the container (default: python)",
    )
    parser.add_argument(
        "--r-path",
        "-r",
        default="R",
        help="Path to R executable inside the container (default: R)",
    )

    args = parser.parse_args()
    return install_singularity_kernel(
        args.image_path,
        args.name,
        args.display_name,
        language=args.language,
        python_path=args.python_path,
        r_path=args.r_path,
    )


if __name__ == "__main__":
    sys.exit(main())
