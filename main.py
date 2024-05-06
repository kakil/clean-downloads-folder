# Python Automatic Downloads Folder Cleaner

"""
1. Find downloads folder
2. Delete files in download folder
3. Delete directories in downloads folder
4. Schedule script to run
"""
import os
import shutil


def clean_downloads():
    download_folder_path = os.path.expanduser("~/Downloads")
    print(download_folder_path)
    downloads_contents = os.listdir(download_folder_path)
    print(downloads_contents)

    for item in downloads_contents:
        item_path = os.path.join(download_folder_path, item)

        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            print("No files or directories present.")





if __name__ == "__main__":
    clean_downloads()