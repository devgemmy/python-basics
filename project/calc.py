# from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":"add",
    "-":"subtract",
    "*":"multiply",
    "/":"divide",
}

new_operations = ("+", "-", "*", "/")

def calculation(operate, fig1, fig2):
    if (operate == "add"): 
        add(fig1, fig2)
    elif (operate == "subtract"):
        subtract(fig1, fig2)
    elif (operate == "multiply"):
        multiply(fig1, fig2)
    elif (operate == "multiply"):
        multiply(fig1, fig2)
    else:
        print("You didn't type in any operator")

def calculator():

    # print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in new_operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        operation_to_do = operations[operation_symbol]
        print(operation_to_do)

        answer = calculation(operation_to_do, num1, num2)
        should_continue = False
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input("Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
        num1 = answer
    else:
        should_continue = False
        calculator()

calculator()