#Calculator Simulator

allowed = "0123456789+-*/(). "

while True:

    print("=" * 40)
    print("SIMPLE PYTHON CALCULATOR")
    print("=" * 40)
    print("1.START")
    print("2.END")
    print("=" * 40)

    choice = int(input("Enter your choice: "))
    print("=" * 40)

    if choice == 1:

        limit = int(input("Enter number if limit for calculation:"))
        print("=" * 40)
        count = 0

        while count < limit:

            expression = input("Enter expression: ")

            if expression == "":
                print("Enter some expression man T~T")
                continue

            if all(char in allowed for char in expression):   #checks if the allowed list is true ot not

                try:
                    result = eval(expression)
                    print("Result =", result)
                    count += 1
                    print(f"Calculations left: {limit - count}")

                except ZeroDivisionError:    # checks if the expression is divided by 0
                    print("Error: Division by zero is not allowed :)")

                except Exception:
                    print("Invalid Expression")

            else:
                print("Only numbers and + - * / ( ) are allowed.")

        print("=" * 40)
        print("You have reached the maximum limit of calculations.")
        print("Returning to main menu...\n")

    elif choice == 2:
        print("Calculator Closed.")
        break

    else:
        print("Invalid Choice!")
