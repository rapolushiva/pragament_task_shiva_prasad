TASK:
=====

    Write a python script that takes 2 jpg image files like attached files(1 empty fill in the blank question paper and 1 filled answer sheet) 
    as inputs and prints/outputs the filled answers in text.With the below example jpg files, output text will be like ans1, ans2, ans3....
    
    
Tip:
=====
    You may want to compare the 2 images pixel by pixel to get the answers from the blanks. Use OCR to extract text from image.
    note that answers may have more than 1 word with space between 2 words.
    
    
    
Libraries Required:
==================
                1)PIL (Python Imaging Library) or Pillow: It provides image processing capabilities, such as opening, manipulating, and saving various image formats.
                  To run below command then Image,ImageChops will import from PIL
                            
                            pip install pillow

                2)ImageChops (from PIL or Pillow): It offers simple arithmetic image operations for pixel-level manipulations like blending, comparison, masking, and more.

                3)cv2 (OpenCV): OpenCV is a powerful library for computer vision tasks. It provides functions for image and video processing, computer vision algorithms, and machine learning.
                  To import cv2 we need to install opencv  run the below command
                  
                  
                           pip install opencv-python
                           
                           

                4)easyocr: This library is used for text recognition (OCR - Optical Character Recognition). It allows you to extract text from images and perform text detection tasks.
                   To import easyocr run the below command 
                    
                            pip install easyocr
       

                5)os: It is a standard Python library that provides operating system-related functionalities, like working with directories, file paths, and more.
                The os module is part of the Python Standard Library, which means you don't need to install any additional libraries to use it. It comes pre-installed with Python,
                 and you can directly import it in your Python scripts.
                 
                
Required Images:
            one image  is empty question paper another one image question paper with answers.
            two images are save at python file folder .if any other place is there then clearly menion the image1_path and image2_path
            
                
Run the code:
            Just run the python code either in any IDE or Terminal or CMD. Then check printed text and output text file.
            
                            python3 main.py
       
        # pragament_task_shiva_prasad
