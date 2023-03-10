import os
items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('work.txt','w')
file.writelines(items)
file.close()