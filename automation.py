import os
import shutil

# Source folder where JPG files are stored
source_folder = "images"

# Destination folder
destination_folder = "jpg_files"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get all files from source folder
files = os.listdir(source_folder)

# Move only JPG files
for file in files:
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All JPG files have been moved successfully!")