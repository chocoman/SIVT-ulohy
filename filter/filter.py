from PIL import Image
import numpy as np

def loadImage(file_path):
    pil_image = Image.open(file_path)
    numpy_image = np.asarray(pil_image)
    #np.array(pic.getdata()).reshape(pic.size[0], pic.size[1], 3)
    print(f'loaded image, dimensions: {numpy_image.shape}')
    return numpy_image

def exportImage(numpy_image, output_path):
    pil_image = Image.fromarray(np.uint8(numpy_image))
    pil_image.show()
    pil_image.save(output_path)
    
image = loadImage('./ludmila.jpg')

# TODO upravit obrazek

exportImage(image, './output.jpg')
