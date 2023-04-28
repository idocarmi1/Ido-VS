import os
import shutil

# Define the input directory
input_dir = input("Enter the path of the directory you want to organize: ")

# Define the output directories for each file type
image_dir = os.path.join(input_dir, "images")
video_dir = os.path.join(input_dir, "videos")
document_dir = os.path.join(input_dir, "documents")

# Create the output directories if they don't exist
os.makedirs(image_dir, exist_ok=True)
os.makedirs(video_dir, exist_ok=True)
os.makedirs(document_dir, exist_ok=True)

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    # Get the full path of the file
    filepath = os.path.join(input_dir, filename)

    # Determine the type of the file
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        # Move the file to the image directory
        shutil.move(filepath, image_dir)
    elif filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
        # Move the file to the video directory
        shutil.move(filepath, video_dir)
    elif filename.endswith((".doc", ".docx", ".pdf", ".txt")):
        # Move the file to the document directory
        shutil.move(filepath, document_dir)

print("Files organized successfully!")
