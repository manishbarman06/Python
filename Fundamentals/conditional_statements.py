print("\n---- if-elif-else statement ----")
color = input("Enter a color: ").lower()

if color not in ["red", "green", "yellow"]:
    print("Invalid Color!")

if color == "red":
    print("STOP!")
elif color == "green":
    print("GO!")
else:
    print("WAIT!")

print("\n---- match statement ----")
dayNum = int(input("Enter a day number: "))

match dayNum:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number!")



