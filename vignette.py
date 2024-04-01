#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:17:37 2023

@author: milica
"""

import numpy as np
import cv2

def get_gauss_kernel(size,sigma):
    center=(int)(size/2)
    kernel=np.zeros((size,size))
    for i in range(size):
       for j in range(size):
          diff=np.sqrt((i-center)**2+(j-center)**2)
          kernel[i,j]=np.exp(-(diff**2)/(2*sigma**2))
    return kernel/np.sum(kernel)

def vignette_img(input_image, sigma_value=200): 
    input_image = cv2.resize(input_image, (600, 600))
    
    rows, cols = input_image.shape[:2]
    
    X_resultant_kernel = get_gauss_kernel(cols, sigma_value)
    Y_resultant_kernel = get_gauss_kernel(rows, sigma_value)
    
    resultant_kernel = Y_resultant_kernel * X_resultant_kernel.T
    
    mask = 255 * resultant_kernel / np.linalg.norm(resultant_kernel)
    output = np.copy(input_image)
    
    for i in range(3):
        output[:,:,i] = output[:,:,i] * mask

    return output