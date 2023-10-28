total = 0 
count = 0 

while True: 

    score = int(input("Enter score, (Enter -9 to end): ") )

    if score != 9: 
        total = total + score
        count = count + 1

    elif score == -9 :
        break

average = float( total ) / count
print("Class average is", average)