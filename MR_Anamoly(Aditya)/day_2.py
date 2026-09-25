#lets make a simple calculator using python


while True:

    print(f"_______________Simple calculator_______________\n  ")
   
    print(f"Select operation number:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
   
    choice = input("Enter choice(1/2/3/4/5): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"SUM OF {num1} AND {num2} IS {num1 + num2}")
    elif choice == '2':
        print(f"DIFFERENCE OF {num1} AND {num2} IS {num1 - num2}")
    elif choice == '3':
        print(f"PRODUCT OF {num1} AND {num2} IS {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"QUOTIENT OF {num1} AND {num2} IS {num1 / num2}")
    elif choice == '5':
        print("Exiting calculator...")
        break
    else:
        print("Invalid input")

    enter = input("press enter to continue")
   
