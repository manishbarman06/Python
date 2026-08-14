try:
    with open(r"D:\CODESPACE\PYTHON\FileHandling\second.txt", "r") as f:
        data = f.read() 

    with open(r"D:\CODESPACE\PYTHON\FileHandling\copied_file.txt", "w") as f:
        f.write(data)

except FileNotFoundError:
    print("ERROR: File Not Found!")
finally:
    print("Program executed...")