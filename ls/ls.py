import os

filelist = os.scandir(os.getcwd())

# ANSI coding for simple colours
BLUE = "\033[1;34m"
END = "\033[0m"

for file in filelist:
    filename = file.name
    
    if filename.find(' ') != -1:
        filename = f"'{filename}'"
    if file.is_dir():
        filename = f"{BLUE}{filename}{END}/"
    print(filename)

