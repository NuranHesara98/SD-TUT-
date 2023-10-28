while True:
    try:
        print("Menu Options:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Quit")

        choice = int(input("Enter your choice (1, 2, 3, or 4): "))

        if choice == 1:
            print("1 selected option")
        elif choice == 2:
            print("2 selected option")
        elif choice == 3:
            print("3 selected option")
        elif choice == 4:
            print("Quit selected option")
            break 
        else:
            print("Option not recognized")
    except ValueError:
        print("Enter an integer choice.")
