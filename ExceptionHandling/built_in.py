try:
    n1 = float(input("Enter dividend: "))
    n2 = float(input("Enter divisor: "))
    res = n1 / n2;
except ZeroDivisionError:
    print("ERROR: Cannot divide by zero!")
except ValueError:
    print("ERROR: Invalid value!")
except TypeError:
    print("ERROR: Typo error!")
else:
    print(f"Result: {n1}/{n2} = {res}")
finally:
    print("Program executed...")


    