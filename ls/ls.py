import os

filelist = os.scandir(os.getcwd())

for file in filelist:
    filename = file.name
    
    if filename.find(' ') != -1:
        filename = f"'{filename}'"
    if file.is_dir():
        filename = f"\033[1;34m {filename}/\033[0m"
    print(filename)

