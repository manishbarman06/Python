'''
Function:
-> A function in Python is a reusable block of organized code 
   designed to perform a specific, isolated task.
-> Functions only execute when they are explicitly called, 
   allowing you to eliminate code repetition and break large programs 
   into smaller, manageable chunks.
-> Functions can accept information as inputs,
   known as parameters during definition, and 
   arguments when the function is called.
   
   Benefits:
   1) Reusability: Write code once and execute it infinitely across your application.
   2) Readability: Keeps projects clean by isolating logic into clearly-named, predictable blocks.
   3) Maintainability: If a calculation ruleset changes, you only have to update it inside its respective function.
'''
print("\n-------- FUNCTIONS --------")
# Function to add two integers
def add(a, b):
    return a + b 
    
print(f"Result: 10 + 20 = {add(10, 20)}")

# *args
print("\n-------- *args --------")
# Function to add numbers
def add(*nums):
    total = 0
    for n in nums:
        total += n
    return total;
    
print(add(10,20,30,40,50))

# **kwargs
print("\n-------- **kwargs --------")
def create_user(**details):
    print(details)
    
create_user(name="Manish", age=19, course="BCA")
create_user(name="Krishna", age=20, course="BCA")

# lambda function 
print("\n-------- Lambda Function --------")
x = 8
y = 5
square = lambda x: x * x
print(f"Square of {x} = {square(x)}")

divide = lambda x, y: x / y
print(f"Division: {x}/{y} = {float(divide(x, y))}")