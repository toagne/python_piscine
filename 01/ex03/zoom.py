from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
	img_arr = ft_load('animal.jpeg')
	print(img_arr)
	channel = img_arr[:, :, 2]
	x_start = img_arr.shape[0] // 2 - 200
	y_start = img_arr.shape[1] // 2 - 200
	sliced = channel[x_start:x_start + 400, y_start:y_start + 400]
	sliced_expanded = sliced[:, :, np.newaxis]
	new_img = Image.fromarray(sliced)
	print(f'New shape after slicing: {sliced_expanded.shape} or {new_img.size}')
	print(sliced_expanded)
	plt.imshow(sliced, cmap='gray')
	plt.xticks([0, 50, 100, 150, 200, 250, 300, 350])
	plt.yticks([0, 50, 100, 150, 200, 250, 300, 350])
	plt.grid(False)
	plt.show()

if __name__ == '__main__':
	main()