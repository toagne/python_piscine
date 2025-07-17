from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def zoom(arr: np.ndarray):
    channel = arr[:, :, 2]
    x_start = arr.shape[0] // 2 - 200
    y_start = arr.shape[1] // 2 - 200
    sliced = channel[x_start:x_start + 400, y_start:y_start + 400]
    return sliced

def main():
    img_arr = ft_load('animal.jpeg')
    sliced = zoom(img_arr)
    sliced_expanded = sliced[:, :, np.newaxis]
    print(f'The shape of image is: {sliced_expanded.shape} or {sliced.shape}')
    print(sliced_expanded)
    new_arr = []
    for x in range(0, len(sliced)):
        line = []
        for y in range(0, len(sliced)):
            line.append(sliced[y][x])
        new_arr.append(line)
    # sliced = sliced.transpose()
    transposed = np.array(new_arr)
    print(f'New shape after transpose: {transposed.shape}')
    print(transposed)
    plt.imshow(transposed, cmap='gray')
    plt.xticks([0, 50, 100, 150, 200, 250, 300, 350])
    plt.yticks([0, 50, 100, 150, 200, 250, 300, 350])
    plt.grid(False)
    plt.show()

if __name__ == '__main__':
    main()