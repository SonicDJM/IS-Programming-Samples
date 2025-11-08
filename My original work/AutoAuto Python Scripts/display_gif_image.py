import numpy as np
from PIL import Image, ImageSequence
import requests
from io import BytesIO
import car
# Download the GIF (make sure your URL is actually a .gif)
url = "https://customemoji.com/images/emojis/meme/nyan-cat.gif"
response = requests.get(url)

# Open the GIF
gif = Image.open(BytesIO(response.content))

# Convert all frames to RGB and then to NumPy arrays
frames = [np.array(frame.convert("RGB")) for frame in ImageSequence.Iterator(gif)]

print(f"Extracted {len(frames)} frames")
print("Frame shape:", frames[0].shape)
print("Frame dtype:", frames[0].dtype)

# Plot each frame using car.plot()
while True:
    for i, frame_array in enumerate(frames):
        print(f"Displaying frame {i}")
        car.plot(frame_array)
