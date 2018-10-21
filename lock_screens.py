import os
import shutil
from pathlib import Path

cwd = os.getcwd()
new_cwd = cwd.split('\\')
user_name = new_cwd[2]


new_folder_location = "/Users/" + user_name + "/Desktop/Copy_Screens"
os.makedirs(new_folder_location)

file_location = "/Users/" + user_name +"/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"


src_dir = os.chdir(file_location)
src_files = os.listdir(src_dir)
for file in src_files:
    shutil.copy(file, new_folder_location)


new_folder = os.chdir(new_folder_location)
dest_files = os.listdir(new_folder)
for new_item in dest_files:
    p = Path(new_item)
    p.rename(p.with_suffix('.jpeg'))
