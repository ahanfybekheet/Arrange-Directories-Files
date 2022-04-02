#---------------------------------------
#  Arrange Directories' Files
# Developed By: Ahmed Hanfy Bekheet 
# Last Modified: 4/2/2022
# Python Version: 3.9.10
# Version : 1.0.0
#---------------------------------------

import os
import shutil


while True:
    dir_path = input("Please, Enter the full path of the directory: ")
    try: os.chdir(dir_path) # Try to go to given path
    except: print("Please, Enter valid path and try again!!..\n\n")
    else: break

for file in os.scandir():
    if file.is_file():
            (name,extension) = (file.name.split('.')[0],file.name.split('.')[-1])
            try: os.mkdir(extension)
            except: pass
            shutil.move(file.name,extension)


