import os
import shutil
import tkinter as tk
from tkinter import filedialog


# Function to cycle through each folder / files
# Note: This does not organize sub-folders
def organize_files(source_folder):
    # Loop through each file in the source folder
    for filename in os.listdir(source_folder):
        # Get the full path of the file
        file_path = os.path.join(source_folder, filename)

        # If path is a directory, we will just use the extension of 'folder' to use a folder named 'folder',
        # instead of a file extension
        if os.path.isdir(file_path):
            file_extension = "folder"

        # If path is a file, we extract the extension and use that to create a folder
        elif os.path.isfile(file_path):
            file_extension = filename.split('.')[-1] if '.' in filename else 'no-extension'

        # If for some reason it's not a file, or directory, just continue
        else:
            continue

        # This is where we create a folder based on the extension.
        folder_name = os.path.join(source_folder, file_extension)
        # Check if directory doesn't exist
        if not os.path.exists(folder_name):
            # We create a directory, but only if it doesn't exist
            os.makedirs(folder_name)

        # Move the file to the appropriate folder
        # We also have to make sure we don't try to move the 'folder' folder into itself
        # This will cause an error, so we just make sure the folder isn't named 'folder'
        if not filename == "folder":
            # Finally we do the file moving
            if os.path.exists(os.path.join(folder_name, filename)):
                # If filename (folder) already exists, we will add a v2 to it
                # That way we won't run into issues when organizing the second loop through
                filename = filename + "-v2"
            # This is where we do the actual move
            shutil.move(file_path, os.path.join(folder_name, filename))


# When the program runs
if __name__ == "__main__":
    # What folder are we organizing?
    source_folder = filedialog.askdirectory()
    print("Organizing Folder: " + source_folder)
    # Let's do the organizing
    # Here, we do the organizing twice
    # First time will sort the files into their own folders
    # Second time will place those folders into the 'folder' folder
    for x in range(1, 3):
        print("Sorting: " + str(x))
        organize_files(source_folder)
    # Mission accomplished. All is well.
    # Once the function is completed, the only folder you should have in the directory
    # is the 'folder' folder. No files at all.
    # If you ran it on the desktop (like myself) you will still have any desktop shortcuts
    # On there. Aside from shortcuts, the only item left is the 'folder' directory.
    print("Files Organized Successfully")
