# Program for basic caluclations
print("*************Basic Calculator*************")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for modulo")

while True:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    while True:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            print(x+y)
        elif choice == 2:
            print(x-y)
        elif choice == 3:
            print(x*y)
        elif choice == 4:
            print(x/y)
        elif choice == 5:
            print(x%y)
        else:
            print("Enter a valid choice!")
            continue
        while True:
            ch = input("Do you want to execute another operation with SAME NUMBER then Press 'Y' for yes or Press 'N' for No:")
            if ch == 'y' or ch == 'Y':
                break
            elif ch == 'n' or ch == 'N':
                break
            else:
                print("Invalid choice!")
        if ch == 'y' or ch == 'Y':
            continue
        else:
            break
    exit = input("Do you want to execute another operation then Press 'Y' for yes or Press 'N' for No to exit:")
    if exit == 'y' or ch == 'Y':
        continue
    else:
        break
print("______Thank You for using our application._______")
