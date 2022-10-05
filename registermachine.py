till = [10, 20, 30, 5]

def main():
    global till
    till.sort()
    till.reverse()
    value = float(input("Input cost:"))
    given = 0
    while True:
        v = float(input("Enter notes provided (enter negative value to stop declaring notes): "))
        if v < 0:
            break
        given += v
    
    difference = given - value
    change = []

    for v in till:
        if (difference - v) >= 0:
            change.append(v)
            difference += -v
    
    if difference == 0:
        print("your change is: ", change)
    else:
        print("impossible to provide change")

    

main()