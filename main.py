#---------------------------------------
#  Arrange Directories' Files
# Developed By: Ahmed Hanfy Bekheet 
# Last Modified: 4/2/2022
# Python Version: 3.9.10
# Version : 1.0.0
#---------------------------------------

import os
import shutil
from prettytable import PrettyTable

def choose_path():
    # Show the directories and make user to choose one from it
    while True:
        print("To Select Folder enter 0.\nEnter -1 To Write the path New Folder.\nEnter -2 To Go Back\n ".title())
        sub_dirs = [[dir.name for dir in os.scandir() if dir.is_dir() ],[dir.path for dir in os.scandir() if dir.is_dir()]] ##first list to make dir list with name seconde one is to make list with pathes.

        table = PrettyTable()
        table.add_column("Index",list(range(1,len(sub_dirs[0])+1))) ##list(range(1,len(sub_dirs[0])+1)) make range equal to len dirs in current path
        table.add_column("Folders",sub_dirs[0])
        table.add_row(["The Current Path Is: ",os.getcwd()])
        print(table)
        #Start Of Validating input of user to make sure that there is no error will raise
        try:
            while True:
                user_input = int(input("Please Choose Folder: "))
                if user_input >= -2 and user_input <= len(sub_dirs[0]):
                    break
                else:
                    print(f"Please Enter Int Between -2 to {len(sub_dirs[0])}.\n")
        except:
            print("Please Enter Int Number.\nAnd Try Agian!!..")
            return choose_path()
        #End Of Validating

        ### Create New Folder And Change Dir To That Folder When User Enter -1
        if user_input == -1:
            while True:
                dir_path =input("Please Enter The Path: ")
                try: os.chdir(dir_path)
                except: print("Please Enter Valid Path And Try Again!!..\n\n")
                else: break
        ### Go to The Parent Dir When User Enter -2
        elif user_input == -2:
            os.chdir("..")
        ### Select Current Path As Download Path 
        elif user_input == 0:
            break
        else:
            os.chdir(sub_dirs[1][user_input-1])

choose_path()


while True:
    user_input = input("Do You Want To Customize Folders Name ? (y/n)\n\n--> ")
    if user_input in ('y','n'):
        break
    else:
        print("Please, Enter y or n and try again!!..\n\n")


for file in os.scandir():
    if file.is_file():
            (name,extension) = (file.name.split('.')[0],file.name.split('.')[-1])
            if user_input == 'y':
                dir_name = input(f"Please, Enter Dir Name For {extension} extension: ")
                try: os.mkdir(dir_name)
                except: print("folder already there!!..")
                shutil.move(file.name,dir_name)
            else:
                try: os.mkdir(dir_name)
                except: pass
                shutil.move(file.name,extension)

                


