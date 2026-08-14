""" Function to convert content of a file into upper case. """
def uppercase_content_file():
    try:
        with open(r"D:\CODESPACE\PYTHON\FileHandling\normal.txt", "r+") as f:
            f.write("this is a text file.\n")
            f.write("i am trying to convert the content into uppercase and lowercase content.\n")
            
        with open(r"D:\CODESPACE\PYTHON\FileHandling\normal.txt", "r") as f:
            data = f.read()
            
        with open(r"D:\CODESPACE\PYTHON\FileHandling\uppercase_content.txt", "w") as f:
            f.write(data.upper())
            
    except FileNotFoundError:
        print("ERROR: File Not Found!")
    finally:
        print("Program executed...")

""" Function to convert content of a file into lower case. """
def lowercase_content_file():
    try:
        with open(r"D:\CODESPACE\PYTHON\FileHandling\uppercase_content.txt", "r") as f:
            data = f.read()
        
        with open(r"D:\CODESPACE\PYTHON\FileHandling\lowercase__content.txt", "w") as f:
            f.write(data.lower())
    
    except FileNotFoundError:
        print("ERROR: File Not Found!")

if __name__=="__main__":
    uppercase_content_file()
    lowercase_content_file()