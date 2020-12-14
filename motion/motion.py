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

def getForegroundMask(frame, background):
    differences = np.mean(np.abs(frame - background), 2)
    foregroundMask = differences >= 15
    return foregroundMask

def removeBackground(frame, background):
    height, width, depth = frame.shape
    newBackground = np.zeros((height, width, depth))
    backgroundMask = getForegroundMask(frame, background) == False
    expandedMask = np.tile(np.reshape(backgroundMask, (height, width, 1)), (1, 1, 3))
    frame[expandedMask] = newBackground[expandedMask]
    return frame

def markArea(i, j, areas, area_id, mask):
    height, width = mask.shape
    if i < 0 or j < 0 or i >= height or j >= width: return
    if (mask[i, j] == False): return
    if (areas[i, j] != 0): return
    areas[i, j] = area_id
    markArea(i, j - 1, areas, area_id, mask)
    markArea(i - 1, j, areas, area_id, mask)
    markArea(i, j + 1, areas, area_id, mask)
    markArea(i + 1, j, areas, area_id, mask)

def identifyAreas(mask):
    height, width = mask.shape
    areas = np.zeros(mask.shape)
    area_id = 1
    for i in range(height):
      for j in range(width):
        # do not search background.
        if (mask[i, j] == False): continue
        # do not search from already marked pixels.
        if (areas[i, j] != 0): continue
        markArea(i, j, areas, area_id, mask)
        area_id += 1
    return areas

frames = loadSequence('coral/coral-', '.png', 55, 216, 384, 3)
print(frames.shape)

background = np.median(frames, 0)

mask = getForegroundMask(frames[7], background)
areas = identifyAreas(mask)

exportImage((areas * 71) % 256 , './output/areas.png')
exportImage(background, './output/background2.png')

for i in range(len(frames)):
    os.makedirs('output', exist_ok=True)
    mask = removeBackground(frames[i], background)
    exportImage(mask, f'./output/mask-{i+1}.png')
