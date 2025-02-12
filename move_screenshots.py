import os
import shutil

# Define paths
desktop_path = os.path.expanduser("~/Desktop")
destination_folder = os.path.join(desktop_path, "Screenshots")  # Change folder name if needed

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get all image files (Screenshots are usually PNGs on macOS)
image_extensions = (".png", ".jpg", ".jpeg")
files_moved = 0

# Move files
for file in os.listdir(desktop_path):
    if file.lower().endswith(image_extensions):
        source_path = os.path.join(desktop_path, file)
        destination_path = os.path.join(destination_folder, file)
        
        shutil.move(source_path, destination_path)
        files_moved += 1
        print(f"Moved: {file}")

if files_moved:
    print(f"\n✅ Moved {files_moved} images to {destination_folder}.")
else:
    print("\n❌ No images found to move.")


