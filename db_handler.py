import os
import shutil
# from PIL import Image
# import imagehash
from pymongo import MongoClient
from hash_util import genHash

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Automation_img"]
collection = db["images"]

# Path to the directory containing images
image_dir = "./Images/new_images"
duplicate_dir = "./Images/duplicates"  # New directory for duplicates

def process_image(image_path):
    image_hash = genHash(image_path)
    # Check if hash already exists in MongoDB
    existing_image = collection.find_one({"hash": image_hash})
    if existing_image:
        # Move the duplicate image to the duplicate directory
        duplicate_path = os.path.join(duplicate_dir, os.path.basename(image_path))
        shutil.copy(image_path, duplicate_path)  # Use shutil.move to keep the original image
    else:
        # Insert new image hash into MongoDB
        collection.insert_one({"hash": image_hash, "path": image_path})
        print(f"New image added: {image_path}")

        # Copy the new image to a new folder
        new_folder = "./Images/new_images"  # Change this to your desired folder
        new_image_path = os.path.join(new_folder, os.path.basename(image_path))
        shutil.copy(image_path, new_image_path)

# Create the duplicate directory if it doesn't exist
os.makedirs(duplicate_dir, exist_ok=True)

# Continuously monitor the image directory for new images
# while True:
#     for filename in os.listdir(image_dir):
#         if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#             image_path = os.path.join(image_dir, filename)
#             process_image(image_path)

# Close the MongoDB connection
# client.close()

