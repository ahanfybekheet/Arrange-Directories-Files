#---------------------------------------
# Arrange Directories' Files Or Change Files' Extention
# Developed By: Ahmed Hanfy Bekheet 
# Last Modified: 5/21/2022
# Python Version: 3.9.10
# Version : 2.0.0
#---------------------------------------

import os
import shutil
from prettytable import PrettyTable

def choose_path():
    '''Change Current Path To Wanted Path Using Os Library From Using'''
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



def arrange_folder():
    while True:
        user_input = input("Do You Want To Customize Folders Name ? (y/n)\n\n--> ")
        if user_input in ('y','n'):
            break
        else:
            print("Please, Enter y or n and try again!!..\n\n")

    for file in os.scandir():
        if file.is_file():
                (name,extension) = (file.name.split('.')[:-1],file.name.split('.')[-1])
                if user_input == 'y':
                    dir_name = input(f"Please, Enter Dir Name For {extension} extension: ")
                    try: os.mkdir(dir_name)
                    except: print("folder already there!!..")
                    shutil.move(file.name,dir_name)
                else:
                    try: os.mkdir(extension)
                    except: pass
                    shutil.move(file.name,extension)



def change_ext():
    ext = input("Please, Enter The New Extention\nBe Informed That this Operation Can't Be Undo..\n->> ")
    table = PrettyTable()
    table.add_column("Index",list(range(1,len(list(os.scandir()))+1)))
    table.add_column("File Name",[file.name for file in os.scandir()])
    table.add_row([len(list(os.scandir()))+1,"Select All"])
    print(table)
    while True:
        user_input = set(map(int,input("Choose File Index That You Want to change it's ext e.g(1,2,3) : ").split(',')))
        valid_input = [x for x in user_input if x >= 1 and x <= len(list(os.scandir()))+1 ]
        if valid_input:
            break
        else:
            print("Please Enter Valid Input..\n")

    if user_input == len(list(os.scandir()))+1:
        for file in os.scandir():
            (name,current_ext) = (str(file.name.split('.')[0:-1]),file.name.split('.')[-1])
            os.rename(file.name,name+f".{ext}")
    else:
        files_name_list = [list(os.scandir())[x-1].name for x in user_input]
        for file_name in files_name_list:
            (name,current_ext) = (str(file_name.split('.')[0:-1]),file_name.split('.')[-1])
            os.rename(file_name,name+f".{ext}")





if __name__ == '__main__':
    print("1-Arrange Folder\n2-Change Files Ext")
    while True:
        user_input = input("->>")
        if user_input == "1" or user_input == "2":
            break
        else:
            print("Ya3m D5l myten valid Inpuuuuut!!!!!\n")
    choose_path()
    if user_input == "1":
        arrange_folder()
    else:
        change_ext()