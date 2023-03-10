import os

path = r'C:\Users\User\Music\PP2\lab 6\dir-and-files\delete.txt'

if os.path.exists(path):
    os.remove(path)
else:
    print("file doesn't exists")
   