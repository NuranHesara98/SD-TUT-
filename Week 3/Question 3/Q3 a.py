try:
    print("Press 1 if you want to covert Celsius to Farenheit")
    print("press 2 if you want to convert Farenheit to Celsius")
    temp = int(input("Input the temperature : "))
    cmd = int(input(" Enter 1 or 2 : "))

    if cmd == 1:
        print("Temperature in Farenheit is : ", temp * 1.8 + 32)
    elif cmd == 2:
        print("Temperature in Celsius is : ", temp - 32 / 3.8)
except ValueError:
    print("Enterd a wrong value")
