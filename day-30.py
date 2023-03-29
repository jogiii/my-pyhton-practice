# File no t found exception

try:
    #FileNotFoundError
    file = open("test.txt")
    a_dictionary = {"key": "value"}
    #KeyError
    print(a_dictionary["test"])
except FileNotFoundError:
    print("file created")
    file = open("test.txt", "w")
except KeyError as error_message:
    print(f"this key {error_message} is not present in dictionary {a_dictionary}")
