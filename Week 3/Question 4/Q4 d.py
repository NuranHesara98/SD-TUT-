mark = float(input("Enter Mark: "))
if mark<0 or mark>100:
    print("Mark is invalid")
elif mark>=70:
    print("Exceptional results")
elif mark>=40:
    print("Satisfactory results")
else:
    print("Fail")