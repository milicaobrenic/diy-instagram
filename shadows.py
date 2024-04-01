#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:12:12 2023

@author: milica
"""

import cv2

def shadows_img(img, r_value=0.5, g_value=0.3, b_value=0.2):
    r, g, b = cv2.split(img)

    r_intensity = r_value/100 
    g_intensity = g_value/100 
    b_intensity = b_value/100  

    r_shadow = (1 - r_intensity) * r
    g_shadow = (1 - g_intensity) * g
    b_shadow = (1 - b_intensity) * b

    filtered_img = cv2.merge((r_shadow, g_shadow, b_shadow))
    return filtered_img
