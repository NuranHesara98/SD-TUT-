import random

hidden = random.randint(1, 20)

print("Welcome to the Guess the Number game!")

while True:
    guess = int(input("Enter a guess (between 1 and 20): ")

    if guess == hidden:
        print("Congratulations! Your guess is correct.")
        break  
    else:
        print("Sorry, your guess is not correct. Try again.")
