'''
Name : Abdul Aziz Muhammad Ibrahim Isa
Roll No : P17-6143
Digital Image Processing Assignment # 2

'''
#all imports here
from PIL import Image, ImageDraw
from os import system
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fp
from scipy import ndimage
import scipy.stats
import math

class ImageProcessing:
    def __init__(self,path):
        image = Image.open(path)
        arrimage = np.array(image)
        self.height, self.width = arrimage.shape
        print("size of input image", arrimage.shape)
        print(arrimage)
        image.show()
        
        #self.imageToFrequency(arrimage)
        #image = self.Laplacian(arrimage)
        #self.SNR(arrimage)
        #self.imageToFrequency(arrimage)
        #image = self.LowPassFilter(arrimage, 300)
        #image = Image.fromarray(image)
        #image.show()
        
        
        
        # Part 2
    def gaussian_kernel(size, sigma=1, verbose=False):
 
        kernel_1D = np.linspace(-(size // 2), size // 2, size)
        for i in range(size):
            kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
        kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)
     
        kernel_2D *= 1.0 / kernel_2D.max()
     
        return kernel_2D
    # Part 1 
    def Laplacian(self,image):
        new_image = np.zeros((self.height,self.width),image.dtype)
        image = np.pad(image,1,mode='constant')
        for i in range(1,(self.height+1)):
            for j in range(1,(self.width+1)):
                new_image[i-1][j-1] = (image[i-1][j] + image[i][j-1] + image[i+1][j] + image[i][j+1]) - (4*image[i][j])
        return new_image
    
    
    # Part 3 
    def SNR(a, axis=None, ddof=0):
        a = np.asanyarray(a)
        m = a.mean(axis)
        sd = a.std(axis=axis, ddof=ddof)
        return np.where(sd == 0, 0, m/sd)
    
    
        # Part 4
    def imageToFrequency(self,image):
        freq = lambda data: fp.rfft(fp.rfft(data, axis=0),axis=1)
        freqx = freq(image)
        return freqx
        
    def D(self,image,u,v):
        return ((u-(len(image)/2))**2 + (v-(len(image[0])/2))**2 )**(0.5)
        
        
        # Part 5
    def HighPassFilter(self, image):
        filters = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
        highpass = ndimage.convolve(image, filters)
        return highpass
    
    
    def LowPassFilter(self,image, cutoff):
        for i in range(len(image)):
            for j in range(len(image[0])):
                if self.D(image,i,j) > cutoff:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        return image
       
    def saveImage(self, image):
        new_im = Image.fromarray(image)
        new_im.save("new_image.tfif")
        
    
        
                                            
if __name__ == "__main__":  
    obj = ImageProcessing('barbara.tif')