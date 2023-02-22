def greeting(name):
  print("Hello, " + name)

import mymodule

mymodule.greeting("Jonathan")


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)

import platform

x = platform.system()
print(x)


import platform

x = dir(platform)
print(x)


def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


from mymodule import person1

print (person1["age"])


#exercises
import mymodule
import mymodule as mx



import mymodule
print(dir(mymodule))


from mymodule import person1