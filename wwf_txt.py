# file = open("data.txt")  # open file -> mount to memory

# print(file.read())

# # memory leaks
# file.close()

# read file with
# with open("data.txt", "r") as f:
#     print(f.read())


# write file with
# with open("data.txt", "w") as f:
#     f.write("Hello world\n")
#     f.write("Hi world!\n")

# append
with open("data.txt", "a") as f:
    f.write("Hello world\n")
    f.write("Hi world!\n")
