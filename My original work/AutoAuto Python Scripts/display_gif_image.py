import numpy as np
from PIL import Image, ImageSequence
import requests
from io import BytesIO
import car  # your display module

# === Configuration: use actual screen resolution
MAX_WIDTH = 480
MAX_HEIGHT = 320

def resize_frame_if_needed(pil_img, max_w=MAX_WIDTH, max_h=MAX_HEIGHT):
    w, h = pil_img.size
    if w <= max_w and h <= max_h:
        return pil_img
    scale = min(max_w / w, max_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    return pil_img.resize((new_w, new_h), Image.ANTIALIAS)

# === Example usage
url = "https://media.tenor.com/5D_DoIfRwFEAAAAM/cat-piano.gif"
response = requests.get(url)
gif = Image.open(BytesIO(response.content))

frames = []
for frame in ImageSequence.Iterator(gif):
    rgb = frame.convert("RGB")
    resized = resize_frame_if_needed(rgb, MAX_WIDTH, MAX_HEIGHT)
    arr = np.array(resized)
    frames.append(arr)

print(f"Extracted {len(frames)} frames, each with shape near {frames[0].shape}")

while True:
    for i, frame_array in enumerate(frames):
        print(f"Displaying frame {i}, shape {frame_array.shape}")
        car.plot(frame_array)
