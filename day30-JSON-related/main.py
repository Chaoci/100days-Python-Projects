# practice
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["asdadsasd"])
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("something")
# except KeyError as error_message:
# 	print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("this is a error that I made up!")

# own exception example

height = float(input("height:"))
weight = int(input("weight:"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")