import os
import subprocess
import sys

def open_directory_in_explorer(directory_path):
    """Opens the given directory in Windows Explorer."""
    try:
        subprocess.run(['explorer', directory_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while opening the directory: {e}")
        sys.exit(1)

def main():
    temp_dir = os.getenv('TEMP', os.path.expanduser('~\\AppData\\Local\\Temp'))
    target_dir = os.path.join(temp_dir, '.soǝnbᴉʇɐɟ')

    if not os.path.exists(target_dir):
        print(f"{target_dir} folder not found.")
        sys.exit(1)

    open_directory_in_explorer(target_dir)

if __name__ == "__main__":
    main()
