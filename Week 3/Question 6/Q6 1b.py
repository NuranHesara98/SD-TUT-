try:
    age = input('Enter your age: ')
    age = int(age)
    if age >= 18:
        print("You can vote")
except ValueError:
    print('Invalid input. Please enter a valid integer for your age.')
