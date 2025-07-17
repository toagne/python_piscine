from PIL import Image
import matplotlib.pyplot as plt

def ft_invert(array):
    """Inverts the color of the image received"""
    arr = array.copy()
    arr[:, :, :] = 255 - arr[:, :, :]
    img = Image.fromarray(arr)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def ft_red(array):
    """Image is now in shades of red"""
    arr = array.copy()
    arr[:, :, 1] = 0
    arr[:, :, 2] = 0
    img = Image.fromarray(arr)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def ft_green(array):
    """Image is now in shades of green"""
    arr = array.copy()
    arr[:, :, 0] = 0
    arr[:, :, 2] = 0
    img = Image.fromarray(arr)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def ft_blue(array):
    """Image is now in shades of blue"""
    arr = array.copy()
    arr[:, :, 0] = 0
    arr[:, :, 1] = 0
    img = Image.fromarray(arr)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def ft_gray(array):
    """Image is now in shades of gray"""
    arr = array.copy()
    arr = array[:, :, 1]
    img = Image.fromarray(arr)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()