# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["rand"]

# IndexError
# TypeError
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     value = a_dict["key"]
# except FileNotFoundError:
#     file = open("a_file.txt", mode='w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is a raised error.")

# height = float(input("Height: "))
# weight = float(input("Weight: "))
# if height > 3:
#     raise ValueError("Human height is not over 3 metres.")
# bmi = weight / height ** 2
# print(bmi)