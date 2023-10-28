num_1 = input("Please enter only integers: ")
num_2 = input("Please enter an integer to devide the number: ")
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 / num_2)
except ZeroDivisionError:
    print("It seams can't devide by 0")