import os

from matplotlib import image
# import PIL.Image as Image
import imagesize
import shutil


# INITIALIZATION
# Image.MAX_IMAGE_PIXELS = 839160000 + 1000   # getting DECOMPRESSION ERROR
allowed_extensions = [".jpg", ".png", ".ico",".tiff",".jpeg",".gif"]


# prompt to ask the user for the path
RootDir = input("Enter directory of icons:\t\n")
# RootDir = "PUT YOUR PATH HERE"    # you can put your path directly here


# folder where all the image files will be stored
targetFolder = input("Enter Path for icons where it will be stored:\t\n")
# targetFolder = "PUT YOUR PATH HERE"   # you can put your path directly here


# PROCESS
for dirPath, dirname, filenames in os.walk(RootDir + "\\"):


        for file in filenames:
            
            if os.path.splitext(file)[1] in allowed_extensions:
            
                filepath = os.path.join(dirPath, file)
            
                try:
                    
                    width , height = imagesize.get(filepath)
                    
                    (f , w, h) = filepath, width, height




                    # if image width and height are less than 12px and greater than 256px and both are equal
                    if (12 <= w <= 256) and (12 <= h <= 256) and (w == h):

                        
                        # error/exception will raise when you put breakpoint here (indulges with os processes)
                        shutil.move(f, targetFolder)
                        
                        
                        print(
                            f'file moved to {targetFolder}\n file: {file}')


                # WARNING never use this procedure. That is a bad practice
                except os.error or shutil.Error or Exception as e:
                    print(f'Error: {e}')
                    """SUGGESTIONS use 'logging' module to collect the exceptions so that
                    you can see in future any errors or warnings"""
                    pass
