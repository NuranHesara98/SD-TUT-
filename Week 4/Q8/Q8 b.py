max_rows=5
for x in range(0,max_rows):
    print(" "*x, end="")
    for y in range(max_rows - x): 
        print('*', end='')
    print()