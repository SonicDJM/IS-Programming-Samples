import numpy as np
from PIL import Image, ImageSequence
import requests
from io import BytesIO
import car

# Download an image of a cat
url = "https://scontent.fftw1-1.fna.fbcdn.net/v/t1.6435-1/166675306_284786423033354_5158251806709613467_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=104&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=-MgsBbWnTNMQ7kNvwHrWVPq&_nc_oc=AdmIAcBQIvltvaLLkuwRTIgAxJs2TqNy19_wM66jPtVBDNI5BWWVzO68e90tw83vYt0&_nc_zt=24&_nc_ht=scontent.fftw1-1.fna&_nc_gid=HzMa-3Y9eEd2AHnCgD3QZQ&oh=00_Afi6cmJ2l90CalqBKv1HU0OmYY9rAzj2Y9dIeh_rq9jaOQ&oe=6936E439"
response = requests.get(url)

# Convert Image to RGB Format
img = Image.open(BytesIO(response.content)).convert("RGB")

# Convert to NumPy array
cat_array = np.array(img)

print("Shape:", cat_array.shape)
print("Dtype:", cat_array.dtype)

# Display the image
car.plot(cat_array)
