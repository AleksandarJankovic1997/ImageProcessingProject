#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:25:12 2021

@author: aleksandar
"""
import numpy as np
from  PIL import Image
from utils import rgb2hsv

class MyImage:
    
    
    def __init__(self, image_path):
        image=Image.open(image_path)
        self.image_path=image_path
        self.arr=np.array(image)
        self.height=self.arr[0].size//3
        self.width=self.arr.size//3//self.height
      
      
    
    def getSize(self):
        return (self.width,self.height)
    
    def open(image_path):
        return  MyImage(image_path)
    
    
    
    
    def save(self,save_image_path):
       image=Image.fromarray(self.arr)
       image.save(save_image_path,quality=80,optimize=True, progressive=False)
    
    def getpixel(self,shape):
        w=shape[0]
        h=shape[1]
        r,g,b=self.arr[w][h]
        return (r,g,b)
        
    def putpixel(self,shape, rgb):
        w,h=shape[0],shape[1]
        r,g,b=rgb[0],rgb[1],rgb[2]
        self.arr[w][h][0]=r
        self.arr[w][h][1]=g
        self.arr[w][h][2]=b
    

    def convert(self):
        print('soon')
        
    def histogramHSV(self):
        histogram=[]
        for i in range (self.height):
            for j in range(self.width):
                r,g,b=self.getpixel((j,i))
                hsv=rgb2hsv(r,g,b)
                histogram[int(hsv[0])]+=1
        return histogram           
     
    def histogramRGB(self):
        histogramrgb=np.zeros((255,3))
        for i in range (self.height):
            for j in range(self.width):
                r,g,b=self.getpixel((j,i))
                histogramrgb[r][0]+=1
                histogramrgb[g][1]+=1
                histogramrgb[b][2]+=1
        return histogramrgb

image=MyImage.open('test.jpg')
image.histogram()
'''w,h=image.getSize()
for i in range(0,h):
    for j in range (0,w):
        image.getpixel((j,i))
        '''

        