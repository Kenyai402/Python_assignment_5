# file_handling_assignment.py

def create_file():
    """Creates a new text file and writes three lines to it."""
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line, with a number: 42\n")
            file.write("Finally, this is the third line.\n")
        print("File 'my_file.txt' created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    """Reads the contents of the text file and displays them on the console."""
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Contents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied while trying to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def append_to_file():
    """Appends three additional lines to the existing file."""
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending a new line: Python is fun!\n")
            file.write("Another line: 100 is a nice round number.\n")
            file.write("Last appended line: Let's keep learning!\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied while trying to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    """Main function to execute the tasks."""
    create_file()  # Create and write to the file
    read_file()    # Read and display the contents
    append_to_file()  # Append more lines to the file
    read_file()    # Read and display the contents again

if __name__ == "__main__":
    main()
