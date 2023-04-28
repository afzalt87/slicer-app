import os
from PIL import Image, ImageOps

input_directory = "/Users/xyz/Downloads/testrf"
output_directory = "/Users/xyz/Downloads/testf3"
output_size = (120, 120)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        original_image = Image.open(os.path.join(input_directory, filename))
        fit_and_resized_image = ImageOps.fit(original_image, output_size, Image.ANTIALIAS)
        fit_and_resized_image.save(os.path.join(output_directory, filename))
