import os
print("Test a path exists or not:")
path = r'C:\Users\User\Music\PP2\lab 6\dir-and-files\a.txt'
print(os.path.exists(path))
path = r'C:\Users\User\Music\PP2\lab 6\dir-and-files\work.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))