#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:11:45 2023

@author: milica
"""

import numpy as np

def rotate_image(img, degrees=180):
    rot_rad = degrees * np.pi / 180.0
    rotate_m = np.array([[np.cos(rot_rad), np.sin(rot_rad)],
                         [- np.sin(rot_rad), np.cos(rot_rad)]])

    h, w, c = img.shape
    rotated_image = np.zeros((h, w, c))

    indices_org = np.array(np.meshgrid(np.arange(h), np.arange(w))).reshape(2, -1)
    indices_new = indices_org.copy()
    indices_new = np.dot(rotate_m, indices_new).astype(int)   
    mu1 = np.mean(indices_new, axis=1).astype(int).reshape((-1, 1))
    mu2 = np.mean(indices_org, axis=1).astype(int).reshape((-1, 1))
    indices_new += (mu2-mu1)  

    t0, t1 = indices_new
    t0 = (0 <= t0) & (t0 < h)
    t1 = (0 <= t1) & (t1 < w)
    valid = t0 & t1
    indices_new = indices_new.T[valid].T
    indices_org = indices_org.T[valid].T

    xind, yind = indices_new
    xi, yi = indices_org
    rotated_image[xi, yi, :] = img[xind, yind, :]

    return rotated_image.astype(np.uint8)



