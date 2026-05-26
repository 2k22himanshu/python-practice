# Functions Practice in Python

# Function to greet user
def greet(name):
    return f"Hello, {name}!"


# Function to add two numbers
def add(a, b):
    return a + b


# Function to calculate square
def square(number):
    return number * number


# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Calling functions
print(greet("Himanshu"))

print("Addition:", add(10, 5))

print("Square:", square(4))

print("Number is:", check_even_odd(7))
