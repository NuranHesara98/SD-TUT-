import random

hidden = random.randint(1, 20)
print("The hidden number is:", hidden)

print("Welcome to the Guess the Number game!")

while True:
    guess = int(input("Enter a guess (between 1 and 20): "))

    if guess == hidden:
        print("Congratulations! Your guess is correct.")
        break  
    elif guess < hidden:
        print("Sorry, your guess is too low. Try again.")
    else:
        print("Sorry, your guess is too high. Try again.")
