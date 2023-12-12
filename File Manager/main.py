# Ist Way: If you have different extension files in a directory,
# it will arrange all these files of same extension in one folder and other in other folders.

import os
import shutil                                          # used to transfer files

path = input("Enter your path : ")

files = os.listdir(path)

for file in files:
    # print(i)                                         # give all files name

    filename, extension = os.path.splitext(file)

    # print(filename)
    # print(extension)

    extension_1 = extension[1:]                        # SLICING
    folder_path = path + "\\" + extension_1

    if os.path.exists(folder_path):
      # shutil.move(source, destination)
      shutil.move(path + "\\" + file, path + "\\" + extension_1 + "\\" + file)

    else:
        os.makedirs(folder_path)
        shutil.move(path + "\\" + file, path + "\\" + extension_1 + "\\" + file)



# 2nd Way : It adding a more functionality in the code

import os
import shutil

def list_files(path="."):
    """List files and directories in the given path."""
    print("Listing files and directories in:", path)
    for item in os.listdir(path):
        print(item)

def create_directory(path, directory_name):
    """Create a new directory."""
    new_directory_path = os.path.join(path, directory_name)
    os.makedirs(new_directory_path)
    print(f"Directory '{directory_name}' created at {new_directory_path}")

def delete_file(file_path):
    """Delete a file."""
    os.remove(file_path)
    print(f"File '{file_path}' deleted")

def copy_file(source_path, destination_path):
    """Copy a file to a new location."""
    shutil.copy2(source_path, destination_path)
    print(f"File copied from '{source_path}' to '{destination_path}'")

def move_file(source_path, destination_path):
    """Move a file to a new location."""
    shutil.move(source_path, destination_path)
    print(f"File moved from '{source_path}' to '{destination_path}'")

def main():
    while True:
        print("\nSimple File Manager Menu:")
        print("1. List files and directories")
        print("2. Create directory")
        print("3. Delete file")
        print("4. Copy file")
        print("5. Move file")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting file manager. Goodbye!")
            break

        path = input("Enter the path (press Enter for current directory): ") or "."

        if choice == "1":
            list_files(path)

        elif choice == "2":
            directory_name = input("Enter the new directory name: ")
            create_directory(path, directory_name)

        elif choice == "3":
            file_name = input("Enter the file name to delete: ")
            file_path = os.path.join(path, file_name)
            delete_file(file_path)

        elif choice == "4":
            source_file = input("Enter the source file path: ")
            destination_path = input("Enter the destination path: ")
            copy_file(source_file, destination_path)

        elif choice == "5":
            source_file = input("Enter the source file path: ")
            destination_path = input("Enter the destination path: ")
            move_file(source_file, destination_path)

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
