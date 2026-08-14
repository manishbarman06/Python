"""
FILE HANDLING
-> File handling in Python is managed primarily through the built-in 
   open() function, which allows you to create, read, update, and delete files on your system.
-> The safest and most efficient way to handle files is by using the 'with' statement (context manager), 
   which automatically closes the file after the block of code executes, preventing resource leaks even if an error occurs.

Essential File Modes:
'r' (Read): Default mode. Opens a file for reading; throws an error if the file doesn't exist.
'w' (Write): Opens a file for writing; creates the file if it doesn't exist or overwrites it completely if it does.
'a' (Append): Opens a file to add new data to the end without deleting existing content.
'x' (Create): Creates a new file; returns an error if the file already exists.
'b' (Binary): Used alongside other modes (e.g., 'rb', 'wb') to handle non-text files like images or audio.
"""
try:
    f = open(r"D:\CODESPACE\PYTHON\FileHandling\first.txt", "w")
except FileNotFoundError:
    print("ERROR: File Not Found!")
else:
    f.write("Hello Everyone!")
    f.close();
    print("File created successfully!")
finally:
    print("Program executed...")