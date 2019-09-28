import matplotlib.pyplot as plt
import numpy as np
from math import exp,pow, pi

def add_noise(img, rate=6):
    img[::rate, ::rate, :] = 1
    return

def gaussfun(dif, sigma):
    return exp(-2*(dif/sigma)**2)/(sigma*pow(2*pi,1/2))

def gausskernel(width, height, sigma):
    kernel = np.ones((width, height))
    for i in range(height):
        for j in range(width):
            dif = (i-(height-1)/2)**2 + (j-(width-1)/2)**2
            kernel[i,j] = gaussfun(dif, sigma)
    kernel/=kernel.sum()
    return kernel

def get_kernel(windos_size):
    kernel = np.ones((windos_size, windos_size))
    kernel/=kernel.sum()
    return kernel


def filter(img, window_size=3):
    img2 = np.zeros_like(img)
    kernel = gausskernel(window_size,window_size,10)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2


def main():
    img = plt.imread("img.png")[:, :, :3]
    add_noise(img)
    img2 = filter(img)
    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()