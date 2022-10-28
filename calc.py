
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


while True:
    # take input from the user
    c= input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if c in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if c == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif c == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif c== '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif c == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
