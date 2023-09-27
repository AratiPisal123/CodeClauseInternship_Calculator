# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    # User menu
    print("Enter your choice:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3'' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' to end the program")

    # Input from the user
    user_input = input("")

    # Check for the exit condition
    if user_input =="5":
        break

    # Check for valid input and perform the corresponding operation
    if user_input in ("1","2","3","4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            print("Result:", add(num1, num2))
        elif user_input == "2":
            print("Result:", subtract(num1, num2))
        elif user_input == "3":
            print("Result:", multiply(num1, num2))
        elif user_input == "4":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please enter a valid option.")
