#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:11:45 2023

@author: milica
"""

import cv2
import numpy as np

def black_white_img(img, value=0.5):
    b, g, r = cv2.split(img)

    intensity = value/100 
    gray = np.clip((intensity * b) + (intensity * g) + (intensity * r), 0, 255).astype(np.uint8)

    gray_image = cv2.merge([gray, gray, gray])
    return gray_image


