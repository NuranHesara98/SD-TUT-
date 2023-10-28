try:
    cost=int(input(" Enter the cost of the meal : "))
    lvl=int(input(" Add a rating 1-Totally satisfied, 2-satisfied, 3-Dissatisfied :  "))

    if lvl == 1:
        print("Your tip is", cost * 20 / 100, "\nTotally satisfied ")
    elif lvl == 2:
        print("Your tip is", cost * 15 / 100, "\nsatisfied")
    elif lvl == 3:
        print("Your tip is", cost * 10 / 100, "\nDissatisfied")
except ValueError:
    print("Entered a wrong value")
