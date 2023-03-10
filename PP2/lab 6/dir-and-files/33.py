import os

path=r'C:\Users\User\Music\PP2\lab 6\dir-and-files\B.txt'

if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(path))