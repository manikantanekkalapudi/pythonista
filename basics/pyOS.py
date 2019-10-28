'''OS Module - Use Underlying Operating System Functionality in Python'''
# import os module
import os
# All the attributes and methods in the os module
# print(dir(os))

# Get current working directory
print(os.getcwd())

# Move/point to a different folder location as current working directory
# os.chdir(r'<path to point to>')
# print(os.getcwd())

# Print all the files and folders in the directory in the cwd
print(os.listdir())

# Create a new folder
# os.makedir('newfolder')  # Creates a new folder in the cwd. Not supported in python 3.7.x
# os.makedirs('newfolder/subdir') # Creates one or more folders to multiple levels
# Print all the files and folders in the directory in the cwd
# print(os.listdir())

# Remove a directory/folder
# os.removedirs('newfolder') # This will remove only one folder and throws error when not empty
# os.removedirs('newfolder/subdir') # This will remove intermediate directories also 
# print(os.listdir())

# Rename the file name
# os.rename('file.txt', 'demo.txt')

# Info about the files
print(os.stat('demo.txt'))

# Get last modified date and time of the file from os.stat
print(os.stat('demo.txt').st_mtime)

from datetime import datetime
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# See all the directory tree and the files
for dirpath, dirnames, filenames in os.walk(top='/home/cyborg/Documents'): # This is a generator that yields a tuple of 3 values (dir path, dir within that path, file in that path)
    print('Current Path: ',dirpath)
    print('Directories: ', dirnames)
    print('Files: ',filenames)
    print()

# Get home dir location from the HOME env variable
print(os.environ.get('HOME')) # There a lot of paths in env variable and we'll grab only 'HOME' path

# Create file in home dir
# Method 1: Concatenation-> os.environ.get('HOME')+'/'+'test.txt'. This leads to a lot of confusion with / and so on
# Method 2: os.path
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path) # This adds all the / exactly and generates a path

# File name from a path
print(os.path.basename('/tmp/test.txt')) # Doesn't have to be a real path

# Dir in the path
print(os.path.dirname('/tmp/test.txt'))

# Both Dir name and File name from a path
print(os.path.split('/tmp/test.txt')) #T his return a tuple

# Check if path exists
print(os.path.exists('/tmp/test.txt')) # Returns False

# Check isFile?
print(os.path.isfile('/tmp/test'))

# Check isDir?
print(os.path.isdir('/tmp/test'))

# Split file name and file extension
print(os.path.splitext('/tmp/test.txt')) # Returns a tuple