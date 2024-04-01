#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:54:03 2023

@author: milica
"""

import cv2

def highlight_correction(img, r_value=0.5, g_value=0.3, b_value=0.2):
    r, g, b = cv2.split(img)

    r_intensity = r_value/100 
    g_intensity = g_value/100  
    b_intensity = b_value/100  

    r_highlights = r + r_intensity * (255 - r)
    g_highlights = g + g_intensity * (255 - g)
    b_highlights = b + b_intensity * (255 - b)

    filtered_img = cv2.merge((r_highlights, g_highlights, b_highlights))

    return filtered_img



