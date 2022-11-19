# with open("day24-open_file/my_file.txt") as file:
#     content = file.read()
#     print(content)


with open("day24-open_file/my_file.txt", "a") as file:
    file.write("\nhi")