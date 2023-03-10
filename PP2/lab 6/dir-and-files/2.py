import os

path=r'C:\Users\User\Music\PP2\lab 6\dir-and-files'

print(os.access(path,os.F_OK))

print(os.access(path,os.R_OK))

print(os.access(path,os.W_OK))

print(os.access(path,os.X_OK))
