import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from skimage import filters
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize

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
    
    
def load_images_from_directory_resize(arr_paths, is_gray=False, dim=(256, 256)):

    arr_images = []

    for img_path in tqdm(arr_paths):
        image = imread(img_path)
        image = resize(image, dim, anti_aliasing=True)
        
        if is_gray: 
            arr_images.append(rgb2gray(image))
        else: 
            arr_images.append(image)
            
    return np.asarray(arr_images)

def load_images_from_directory(arr_paths, is_gray=False):

    arr_images = []

    for img_path in tqdm(arr_paths):
        image = imread(img_path)

        if is_gray: 
            arr_images.append(rgb2gray(image))
        else: 
            arr_images.append(image)
            
    return np.asarray(arr_images)