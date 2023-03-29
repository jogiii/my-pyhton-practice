# File no t found exception

try:
    file = open("test.txt")
except:
    print("file created")
    file = open("test.txt", "w")
