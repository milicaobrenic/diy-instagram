#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:11:45 2023

@author: milica
"""
import numpy as np

def blur_img(img, kernel_size=3):
        kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size*kernel_size)
        output_img = filter2D_RGB(img, kernel)
        return output_img
 
def filter2D_RGB(image, kernel):
    rows, cols = image.shape[:2]
    krows, kcols = kernel.shape[:2]

    pad_height = int((krows - 1) / 2)
    pad_width = int((kcols - 1) / 2)

    padded_image = np.zeros((rows + 2 * pad_height, cols + 2 * pad_width, 3), dtype=image.dtype)
    padded_image[pad_height:pad_height+rows, pad_width:pad_width+cols, :] = image

    filtered_image = np.zeros_like(image)

    for channel in range(3):
        for y in range(rows):
            for x in range(cols):
                patch = padded_image[y:y+krows, x:x+kcols, channel]
                filtered_pixel = np.sum(patch * kernel)
                filtered_image[y, x, channel] = filtered_pixel

    return filtered_image

