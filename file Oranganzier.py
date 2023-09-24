import os       # provides functions for interacting with the operating system.
import shutil   # used to perform high-level operations on files and collections of files.

path = input("enter the file path")  # used to take the input
files = os.listdir(path)  # list all the files/directory present in the
for file in files:
    filename, extension = os.path.splitext(file)  # filename = download extension = .jpeg
    print(filename + extension)
    extension = extension[1:]    # remove dot from .jpeg = jpeg

    if os.path.exists(path+'/'+extension):  # check if the folder for the extension exist or not
        shutil.move(path+'/' + file, path+'/'+extension+'/'+file)  # if exist move the file, shutil.move(source, destination)

    else:
        os.makedirs(path+'/'+extension)  # if not make a directory
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)  # and move the file
