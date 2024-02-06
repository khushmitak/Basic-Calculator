#Step 1: Get the user inputs for two numbers and operations.
#Step 1a: check for valid input for number1 and number2
number1 = 0
number2 = 0

def get_valid_numbers(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter the valid floating-point numbers. ")

number1 = get_valid_numbers("Please enter a number: ")
number2 = get_valid_numbers("Please enter another number: ")

#Step 2: Get the user input for operation
print("Please enter the operation you would like to perform")
operation = input("such as: +, -, *, /: ")
    
#Step 3: Check if the operation entered by the user is valid or not
def is_valid_operation(operation):
    valid_operators = ['+', '-', '*', '/']
    
    if operation in valid_operators:
        return True
    else:
        return False

#Step 4: If an invalid operation, keep asking the user to input an operation till we get a valid input 
#use a while loop to do so .
while not is_valid_operation(operation):
    print("Invalid operation. Please try again. ")
    print("Please enter the operation you would like to perform")
    operation = input("such as: +, -, *, /: ")  

#Step 5: If everything is valid, then proceed to perform the operation on two numbers.
def perform_operation(number1, number2, operation):
    result = 0
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    else: #step 5a: fix the zerodivision error when denominator is zero
        try:
            result = number1 / number2
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero. ")
            exit()
            
    return result

#Step 6: Print the result of the operation performed.
res = perform_operation(number1, number2, operation)
print(f"{number1} {operation} {number2} = {res} ")
