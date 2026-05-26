# If-Else in Python

# Check if number is positive or negative
number = int(input("Enter a number: "))

if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# Check voting eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Check even or odd
num = int(input("Enter another number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
