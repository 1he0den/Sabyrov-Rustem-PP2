
import os
import string

# 1

# def list_contents(path):
#     if not os.path.exists(path):
#         print(f"The path '{path}' does not exist.")
#         return
    
#     dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
#     files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
#     print("\nDirectories:", dirs)
#     print("\nFiles:", files)
#     print("\nAll Contents:", os.listdir(path))

# path = input("Enter the directory path: ")
# list_contents(path)

# 2

# def check_access(path):
#     print("\nAccess Permissions:")
#     print(f"Exists: {os.path.exists(path)}")
#     print(f"Readable: {os.access(path, os.R_OK)}")
#     print(f"Writable: {os.access(path, os.W_OK)}")
#     print(f"Executable: {os.access(path, os.X_OK)}")

# path = input("Enter the directory path: ")
# check_access(path)

# 3

# def path_info(path):
#     if os.path.exists(path):
#         print("\nPath Information:")
#         print(f"Directory Portion: {os.path.dirname(path)}")
#         print(f"Filename Portion: {os.path.basename(path)}")
#     else:
#         print("The specified path does not exist.")

# path = input("Enter the directory path: ")
# path_info(path)

# 4

# def line_counter(path):
#     count_of_line = sum(1 for _ in open(path)) + 1
#     print(f"\nThe number of lines in the file '{path}' is {count_of_line}.")

# path = input("Enter the file path: ")
# line_counter(path)


# 5

# def write_list_to_file(file_path, data_list):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.writelines(f"{item}\n" for item in data_list)
#     print(f"List written to '{file_path}'.")

# file_path = input("Enter the file path: ")
# data_list = input("Enter the list of data: ").split()
# write_list_to_file(file_path, data_list)


# 6

# def generate_text_files():
#     for letter in string.ascii_uppercase:
#         file_name = f"{letter}.txt"
#         with open(file_name, 'w', encoding='utf-8') as file:
#             file.write(f"This is file {file_name}\n")
#         print(f"File '{file_name}' created.")

# generate_text_files()


# 7

# def copy_file(source, destination):
#     with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
#         dest.write(src.read())
#     print(f"Contents copied from '{source}' to '{destination}'.")

# source = input("Enter the source file path: ")
# destination = input("Enter the destination file path: ")
# copy_file(source, destination)


# 8

# def delete_file(file_path):
#     if os.path.exists(file_path) and os.access(file_path, os.W_OK):
#         os.remove(file_path)
#         print(f"File '{file_path}' deleted successfully.")

# file_path = input("Enter the file path: ")
# delete_file(file_path)

