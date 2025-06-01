import os

for index, file in enumerate(os.listdir("image_stack")):
    os.rename(f"image_stack/{file}", f"image_stack/{index}.png")