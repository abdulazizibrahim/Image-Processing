'''
Name : Abdul Aziz Muhammad Ibrahim Isa
Roll No : P17-6143
Digital Imaga Processing Assignment # 1

'''
#all imports here
from PIL import Image
from os import system
import numpy as np
import math
import time


class ImageProcessing:
    def __init__(self, path):  
        image = Image.open(path)
        arrimage = np.array(image)
        print("size of input image", arrimage.shape)
        image.show()
       
        while True:
            time.sleep(2.4)
            system("cls")
            x = int(input("press 1 for flip\n press 2 for negative\n press 3 for bitplane \n press 4 for contrast \n press 5 for thresholding \n press 6 for PLT \n press 7 for contrast stretching \n press 8 for entropy \n press 9 to save image\n press 0 to exit\n"))
            if x == 1:
                newim = self.flip(arrimage)
                newim = Image.fromarray(newim)
                newim.show()
            elif x == 2:
                newim = self.negativeImage(arrimage)
                newim = Image.fromarray(newim)
                newim.show()
            elif x == 3:
                y = int(input("enter plane number 1-8"))
                newim = self.bitPlane(arrimage, y)
                newim = Image.fromarray(newim)
                newim.show()
            elif x == 4:
                newim = self.contrast(arrimage)
            elif x == 5:
                newim = self.thresholding(arrimage)
                newim = Image.fromarray(newim)
                newim.show()
            elif x == 6:
                g = float(input("enter gamma value"))
                newim = self.powerLawTransformation(arrimage, g)
                newim = Image.fromarray(newim)
                newim.show()
            elif x == 7:
                newim = self.contrastStretching(arrimage)
                newim = Image.fromarray(newim)
                newim.show()
            elif x == 8:
                newim = self.entropy(arrimage)
            elif x == 9:
                newim = self.saveImage(arrimage)
            else:
                break
            
    
        
    def flip(self, image):
        rez = image[::-1]
        image = np.array(rez)
        return image
    
    def contrast(self, image):
        brightness = self.brightness(image)
        M = float(len(image))
        N = float(len(image[0]))
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                image[i][j] = float(((1/(M*N)) * (float(image[i][j]) - brightness)**2)**(1/2))
        maxc = np.max(image)
        minc = np.min(image)
        print("constrast value ==>", maxc-minc)
        return
        
    def brightness(self, image):
        total = 0.0
        for rows in image:
            for pixels in rows:
                total += pixels
        total =(1/(len(image)*len(image[0])))*total
        return total


    def negativeImage(self,image):
        negimage = []
        for rows in image:
            negarr = []
            for pixels in rows:
                negarr.append(255-pixels)
            negimage.append(negarr)
        negimage = np.array(negimage)
        return negimage
        
    def bitPlane(self,image, plane):
        maxs = np.max(image)
        x = math.ceil(math.log((maxs + 1), 2))
        if plane > 8 or plane > x:
            print("wrong plane value")
            
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                binary = bin(image[i][j])
                binary = binary[2:]
                binary = "0b" + binary[-(plane):]
                image[i][j] = int(binary, 2)
        return image
                
    def averageIntensity(self,image):
        total = 0
        nump = len(image) * len(image[1])
        print(nump)
        for rows in image:
            for pixels in rows:
                total += pixels
        return (total/nump)
        
    def thresholding(self,image):
        avg = self.averageIntensity(image)
        for i in range (len(image)):
            for pixels in range (len(image[0])):
                    if image[i][pixels] > avg:
                        image[i][pixels] = 255
                    else:
                        image[i][pixels] = 0
        return image
    
    def powerLawTransformation(self,image, gamma):
        for i in range (len(image)):
            for pixels in range (len(image[0])):
                        image[i][pixels] = image[i][pixels]**gamma
        return image
    
    def contrastStretching(self,image):
        Mmin = np.min(image)
        Mmax = np.max(image)
        for i in range (len(image)):
            for pixels in range (len(image[0])):
                        image[i][pixels] = (((255-0)*(image[i][pixels] - Mmin))/(Mmax - Mmin))
        return image
    
    def entropy(self, image):
        probs = []
        total = len(image) * len(image[1])
        for i in range(0, 256):
            count = 0.0
            for rows in image:
                if i in rows:
                    count += 1
            
            probs.append(float(count)/float(total))
        
        entropy = 0
        for i in range(0, 256):
            if probs[i] != 0:
                entropy += (probs[i] * math.log(probs[i], 2))
        entropy = entropy*(-1)
        print(entropy)
        
    def saveImage(self, image):
        new_im = Image.fromarray(image)
        new_im.save("new_image.bmp")
                                            
if __name__ == "__main__":  
    obj = ImageProcessing('lena_gray.bmp')
