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

def removeBackground(frame, background):
    height, width, depth = frame.shape
    flippedBackground = np.flip(background, 1)
    differences = np.mean(np.abs(frame - background), 2)
    backgroundMask = differences < 10
    expandedMask = np.repeat(np.reshape(backgroundMask, (height, width, 1)), axis=2, repeats=3)
    frame[expandedMask] = flippedBackground[expandedMask]
    return frame

frames = loadSequence('coral/coral-', '.png', 55, 216, 384, 3)
print(frames.shape)

background = np.median(frames, 0)


exportImage(background, './output/background2.png')

for i in range(len(frames)):
    os.makedirs('output', exist_ok=True)
    mask = removeBackground(frames[i], background)
    exportImage(mask, f'./output/mask-{i+1}.png')
