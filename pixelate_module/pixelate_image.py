# Script to pixelate an image

from skimage import io
from pyxelate import Pyx, Pal

def get_image_path():
    # ask user for image path
    path = input("Enter the path of the image: ")
    return path

def pixelate_image(image):
    # we take the image name without the extension
    img_name = image.split(".")[0]
    # we take the image extension
    img_ext = image.split(".")[1]
    
    img = io.imread(image)

    # new image will be 1/14th of the original in size
    palette = 7  # find 7 colors

    # 1) Instantiate Pyx transformer
    pyx = Pyx(palette=palette)
    
    print("Image is pixelated.. Please wait..")

    # 2) fit an image, allow Pyxelate to learn the color palette
    pyx.fit(img)

    # 3) transform image to pixel art using the learned color palette
    new_image = pyx.transform(img)

    # save new image with 'skimage.io.imsave()'
    # we add '_pixelated' to the image name
    io.imsave(img_name + "_pixelated." + img_ext, new_image)

    print("Image pixelated successfully!")

    return new_image
    
# main function
def main():
    path = get_image_path()
    image = pixelate_image(path)
