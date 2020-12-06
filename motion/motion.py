from PIL import Image
import numpy as np
import os

def loadImage(file_path):
    pil_image = Image.open(file_path)
    numpy_image = np.asarray(pil_image, np.int)
    return numpy_image

def loadSequence(prefix, suffix, length, height, width, color_depth):
    video = np.zeros((length, height, width, color_depth))
    for i in range(length):
        image = loadImage(prefix + str(i+1) + suffix)
        video[i, :, :, :] = image
    # gray = np.sum(video,3) / 3
    # return gray
    return video

def exportImage(numpy_image, output_path):
    pil_image = Image.fromarray(np.clip(np.uint8(numpy_image), 0, 255))
    pil_image.save(output_path)
    
frames = loadSequence('coral/coral-', '.png', 55, 216, 384, 3)
print(frames.shape)

# TODO process video...

for i in range(len(frames)):
    os.makedirs('output', exist_ok=True)
    exportImage(frames[i], f'./output/debug-{i+1}.png')