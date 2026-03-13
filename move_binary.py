#!/usr/bin/env python3
"""
Script to move the APK binary from master branch to data branch
Used in GitHub Actions workflow
"""

import os
import sys
import shutil
from pathlib import Path


def main():
    if len(sys.argv) != 5:
        print("Usage: move_binary.py <apk_path> <master_branch_dir> <data_branch_dir> <output_dir>")
        sys.exit(1)

    apk_path = sys.argv[1]
    master_dir = sys.argv[2]
    data_dir = sys.argv[3]
    output_dir = sys.argv[4]

    # Create output directory if it doesn't exist
    output_path = Path(data_dir) / output_dir
    output_path.mkdir(parents=True, exist_ok=True)

    # Copy APK to output directory
    apk_filename = Path(apk_path).name
    destination = output_path / apk_filename
    shutil.copy2(apk_path, destination)

    print(f"APK copied to: {destination}")


if __name__ == "__main__":
    main()
