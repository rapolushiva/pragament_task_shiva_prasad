#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:23:15 2023

@author: dragon
"""

from PIL import Image, ImageChops
import cv2
import easyocr
import os

def blank_text_extraction(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    diff_image = ImageChops.difference(image1, image2)
    diff_image_path = "difference_image.jpg"
    diff_image.save(diff_image_path)
    reader = easyocr.Reader(['en'])
    image = cv2.imread(diff_image_path)
    contrasted_image = cv2.convertScaleAbs(image, alpha=2)
    result = reader.readtext(contrasted_image)
    os.remove(diff_image_path)
    return result

if __name__ == "__main__":
    if 'output_text_file.txt' in os.listdir('./'):
        os.remove('output_text_file.txt')

    image1_path = "Fill in the blanks empty sheet.jpg"
    image2_path = "Fill in the blanks answe1.jpeg"
    text_list = blank_text_extraction(image1_path, image2_path)
    for text in text_list:
        line = text[1]+'\n'
        print(line)
        with open('output_text_file.txt', "a") as file:
            file.write(line)
