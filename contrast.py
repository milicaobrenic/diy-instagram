#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:11:45 2023

@author: milica
"""

import numpy as np
import cv2

def contrast_img(image, r_value=1.5, g_value=1.5, b_value=1.5):
    b, g, r = cv2.split(image)

    r_alpha = r_value/10 
    g_alpha = g_value/10
    b_alpha = b_value/10
    b = np.clip(b * b_alpha, 0, 255).astype(np.uint8)
    g = np.clip(g * g_alpha, 0, 255).astype(np.uint8)
    r = np.clip(r * r_alpha, 0, 255).astype(np.uint8)

    new_image = cv2.merge([b, g, r])
    return new_image