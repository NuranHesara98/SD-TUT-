response = input('Do you like Python? (yes/no): ').lower()

if response in ['yes', 'y']:
    print("You are on the right course.")
elif response in ['no', 'n']:
    print("You might change your mind.")
else:
    print("I did not understand your response.")
