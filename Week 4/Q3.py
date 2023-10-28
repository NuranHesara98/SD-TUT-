while True:
    n = input("Please enter an integer: ")
    try:
        n = int(n)
        break
    except ValueError:
        print("invalid Please try again")

print("successfully entered an integer")
