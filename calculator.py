#Step 1: Get the user inputs for two numbers and operations.
number1 = float(input("Please enter a number: "))
number2 = float(input("Please enter another number: "))
print("Please enter the operation you would like to perform")
operation = input("such as: +, -, *, /: ")
    
#Step 2: Check if the operation entered by the user is valid or not
def is_valid_operation(operation):
    valid_operators = ['+', '-', '*', '/']
    
    if operation in valid_operators:
        return True
    else:
        return False

#Step 3: Print if the operation is valid or invalid
if is_valid_operation(operation):
    print("The operation is valid! ")
else: 
    print("Invalid operation. Please try again. ")

#Step 4: If an invalid operation, keep asking the user to input an operation till we get a valid input 
#use a while loop to do so .
while not is_valid_operation(operation):
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
            
    return result

#Step 6: Print the result of the operation performed.
res = perform_operation(number1, number2, operation)
print(f"{number1} {operation} {number2} = {res} ")
