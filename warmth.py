#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:37:19 2023

@author: milica
"""

import cv2
import numpy as np

def warmth_img(img, r_value=0.2, g_value=0.5, b_value=0.8):
    r, g, b = cv2.split(img)

    r_intensity = r_value/100  
    g_intensity = g_value/100 
    b_intensity = b_value/100 

    r_warmth = np.uint8(np.clip((r * (1 + r_intensity)), 0, 255))
    g_warmth = np.uint8(np.clip((g * (1 + g_intensity)), 0, 255))
    b_warmth = np.uint8(np.clip((b * (1 + b_intensity)), 0, 255))

    filtered_img = cv2.merge((r_warmth, g_warmth, b_warmth))
    return filtered_img