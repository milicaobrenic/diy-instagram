#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:11:45 2023

@author: milica
"""

import cv2
import numpy as np

def brightness_img(image, r_value=50, g_value=50, b_value=50):
    b, g, r = cv2.split(image)

    r_beta = r_value 
    g_beta = g_value
    b_beta = b_value
    b = np.clip(b + b_beta, 0, 255).astype(np.uint8)
    g = np.clip(g + g_beta, 0, 255).astype(np.uint8)
    r = np.clip(r + r_beta, 0, 255).astype(np.uint8)

    new_image = cv2.merge([b, g, r])
    return new_image
