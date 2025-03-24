def calculator():
    num1 = float(input("enter the first number"))
    num2 = float(input("enter the second number"))
    operation = input("choose an operation (+, -, *, /)")

    if operation == '+':
        results = num1 + num2
        print(f"{num1} + {num2} = {results}")

    elif operation =='-':
        results = num1 - num2
        print(f"{num1} - {num2} = {results}")

    elif operation =='*':
        results = num1 * num2
        print(f"{num1} * {num2} = {results}")

    elif operation =='/':
        results = num1 / num2
        print(f"{num1} /{num2} = {results}")

    
calculator()




    