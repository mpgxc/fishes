from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from skimage import filters

def binarize_image(arr):
    return arr > filters.threshold_triangle(arr)

def plot(arr_images=[], grid=(2, 2), cmap="inferno"):

    fig = plt.figure(figsize=(20, 10))

    grid = ImageGrid(fig, 111,
                     nrows_ncols=grid,
                     axes_pad=0.1)

    for ax, img in zip(grid, arr_images):
        ax.imshow(img, cmap)
        ax.axis('off')

    plt.show()