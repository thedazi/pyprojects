##Calculator
from Day10art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1%n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

print(logo)

#used for recursion
def calculator():
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    continue_run = True

    while continue_run == True:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calc_function = operations[operation_symbol]
        answer = float(calc_function(num1,num2))
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            continue_run = False
            calculator()
        