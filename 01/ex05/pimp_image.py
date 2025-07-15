from PIL import Image
import matplotlib.pyplot as plt

def ft_invert(array):
    """Inverts the color of the image received"""
    array[:, :, :] = 255 - array[:, :, :]
    img = Image.fromarray(array)
    plt.imshow(img)
    plt.show()

def ft_red(array):
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    img = Image.fromarray(array)
    plt.imshow(img)
    plt.show()

def ft_green(array):
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    img = Image.fromarray(array)
    plt.imshow(img)
    plt.show()

def ft_blue(array):
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    img = Image.fromarray(array)
    plt.imshow(img)
    plt.show()

def ft_gray(array):
    array = array[:, :, 1]
    img = Image.fromarray(array)
    plt.imshow(img, cmap='gray')
    plt.show()