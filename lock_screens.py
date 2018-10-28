import os
import shutil
from pathlib import Path

#Return the user name as a string
def get_user_name():
    cwd = os.getcwd()
    split_cwd = cwd.split('\\')
    user_name = split_cwd[2]
    return user_name

#Create a new folder on the desktop called "Copy Screens"
#Return the path of "Copy Screens" as a string
def create_new_folder(user_name):
    new_folder_location = "/Users/" + user_name + "/Desktop/Copy_Screens"
    if os.path.isdir(new_folder_location):
        print("There is already a folder on your desktop called \"Copy_Screens\".",
                "Would you like to replace this folder?")
        user_response = input("(y/n) > ")
        if user_response == "y" or user_response == "Y":
            shutil.rmtree(new_folder_location)
            os.makedirs(new_folder_location)
        elif user_response == "n" or user_response =="N":
            print("OK Bye!")
            exit()
        else:
            print("You must answer with either a \"Y\" or a \"N\".")
            return create_new_folder(user_name)
    else:
        os.makedirs(new_folder_location)
    return new_folder_location

#Copy windows lockscreens to "Copy Screens"
def copy_files(user_name, new_folder_location):
    file_location = "/Users/" + user_name +"/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
    src_dir = os.chdir(file_location)
    src_files = os.listdir(src_dir)
    for file in src_files:
        shutil.copy(file, new_folder_location)

#Change the extension of each file to add ".jpeg"
def add_jpeg(new_folder_location):
    new_folder = os.chdir(new_folder_location)
    dest_files = os.listdir(new_folder)
    for new_item in dest_files:
        p = Path(new_item)
        p.rename(p.with_suffix('.jpeg'))

def main():

    user_name = get_user_name()

    new_folder_location = create_new_folder(user_name)

    copy_files(user_name, new_folder_location)

    add_jpeg(new_folder_location)


main()
