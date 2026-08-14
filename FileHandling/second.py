try:
    """ Reading and writing to a file """
    with open(r"D:\CODESPACE\PYTHON\FileHandling\second.txt", "r+") as f:
        f.write("This is a second text file in Python.\n")
        f.write("Using 'with' statement file will closed automatically.\n")
        f.write("'with' statement prevents memory leaks too.\n")
        
    """ Appending more content to a file """
    new_content = (
        "Appending someore content at the end of the file.\nUsing append mode 'a'\n"
        )
        
    with open("second.txt", "r") as f:
        existing_content = f.read()
        
    # Checking if content is already exists or not 
    if new_content not in existing_content:
        with open("second.txt", "a") as f:
            f.write(new_content)
        
    """ Reading from a file """
    with open("second.txt", "r") as f:
        print(f.read())
        
except FileNotFoundError:
    print("ERROR: File not found!")
finally:
    print("Program executed...")