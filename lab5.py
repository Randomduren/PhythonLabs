import os

def myfunc(path):
    files = os.listdir(path)
    return (files)

directory = input()
print(myfunc(directory))
