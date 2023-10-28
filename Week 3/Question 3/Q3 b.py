try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    op = input("Enter an operator: ")
    
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(num1 / num2)
    else:
        print("Invalid operator")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
