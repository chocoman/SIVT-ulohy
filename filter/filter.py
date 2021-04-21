from PIL import Image
import numpy as np

def loadImage(file_path):
    pil_image = Image.open(file_path)
    numpy_image = np.asarray(pil_image, np.int32)
    #np.array(pic.getdata()).reshape(pic.size[0], pic.size[1], 3)
    print(f'loaded image, dimensions: {numpy_image.shape}')
    return numpy_image

def exportImage(numpy_image, output_path):
    pil_image = Image.fromarray(np.uint8(numpy_image))
    pil_image.show()
    pil_image.save(output_path)

def darken(image):
    darkened = image - 50
    darkened[darkened < 0] = 0
    return darkened

def darken2(image):
    bw = (image[:,:,0] + image[:,:,1] + image[:,:,2])/3
    bw[bw > 150] = bw[bw > 150] - 150
    return bw

def gradient(image):
    darkening = 0
    for i in range(image.shape[0]):
        darkening = 200 * i / image.shape[0]
        image[i] = image[i] - darkening
    image[image < 0] = 0
    return image

image = loadImage('./ludmila.jpg')
#print(image)
#black_and_white = (image[:,:,0] + image[:,:,1] + image[:,:,2])/3
#rotated = np.rot90(image)
#negative = 255-image
#combined = np.concatenate((image, image), axis=1)
#flipped = np.flip(image, axis=0)
#cropped = image[:250,:,:]
#dark = darken(image)
#dark2 = darken2(image)
grad = gradient(image)
exportImage(grad, './output.jpg')
