import hashlib
import os
from PIL import Image

def genHash(path):
    img =  Image.open(path)
    bytes = img.tobytes()
    readable_hash = hashlib.sha256(bytes).hexdigest()
    return readable_hash
    # print(readable_hash)
    # os.remove(path)