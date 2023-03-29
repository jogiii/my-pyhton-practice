#File no t found exception

try:
    file = open("test.txt")
except:
    print("this file is not found")