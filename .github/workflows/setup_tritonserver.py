import os
import shutil
import subprocess
import sys
from pathlib import Path

def install_pytriton():
    # Install nvidia-pytriton package
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nvidia-pytriton"])

def find_tritonserver_files():
    # Search for the installed pytriton package
    site_packages_dir = Path(next(p for p in sys.path if 'site-packages' in p))
    pytriton_path = site_packages_dir / 'pytriton'
    
    # Check the existence of the required directories
    expected_dirs = ['backends', 'caches', 'bin', 'python_backend_stubs']
    for directory in expected_dirs:
        dir_path = pytriton_path / 'tritonserver' / directory
        if not dir_path.exists():
            raise FileNotFoundError(f"Expected directory {directory} not found in {pytriton_path / 'tritonserver'}")

    return pytriton_path / 'tritonserver'

def copy_files_to_expected_path(src_path, dst_path):
    # Ensure the destination path exists
    os.makedirs(dst_path, exist_ok=True)

    # Copy all contents from the source path to the destination path
    for item in src_path.iterdir():
        s = src_path / item.name
        d = dst_path / item.name
        if s.is_dir():
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def main():
    # Step 1: Install nvidia-pytriton
    install_pytriton()

    # Step 2: Locate the tritonserver files
    tritonserver_files_path = find_tritonserver_files()

    # Step 3: Define the expected path
    expected_path = Path('/home/runner/work/pytriton/pytriton/pytriton/tritonserver')

    # Step 4: Copy the files to the expected path
    copy_files_to_expected_path(tritonserver_files_path, expected_path)

    print(f"Files successfully copied to {expected_path}")

if __name__ == "__main__":
    main()
