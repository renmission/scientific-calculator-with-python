import math

while True:
    print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")

    oper = input("\nYour option from the menu: ")

    # addition
    if oper == "0":
        val1 = float(input("\nEnter first value: "))
        val2 = float(input("\nEnter second value: "))

        print("\nThe result is: " + str(val1 + val2) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # subtraction
    elif oper == "1":
        val1 = float(input("\nEnter first value: "))
        val2 = float(input("\nEnter second value: "))

        print("\nThe result is: " + str(val1 - val2) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # multiplication
    elif oper == "2":
        val1 = float(input("\nEnter first value: "))
        val2 = float(input("\nEnter second value: "))

        print("\nThe result is: " + str(val1 * val2) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # division
    elif oper == "3":
        val1 = float(input("\nEnter first value: "))
        val2 = float(input("\nEnter second value: "))

        print("\nThe result is: " + str(val1 / val2) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # modulo
    elif oper == "4":
        val1 = float(input("\nEnter first value: "))
        val2 = float(input("\nEnter second value: "))

        print("\nThe result is: " + str(val1 % val2) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # raising to a power
    elif oper == "5":
        val1 = float(input("\nEnter first value: "))
        val2 = float(input("\nEnter second value: "))

        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # square root
    elif oper == "6":
        val1 = float(input("\nEnter the value for extracting square root: "))

        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # logarithm
    elif oper == "7":
            val1 = float(input("\nEnter the value for calculating the logarithm for the base 2: "))

            print("\nThe result is: " + str(math.log(val1, 2)) + "\n")

            # back to the main menu or exiting the program
            back = input("\nGo back to the main menu?, (y/n): ")

            if back == "y":
                continue
            else:
                break

    # Sine
    elif oper == "8":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin((math.radians(val1)))) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))

        print("\nThe result is: " + str(math.cos((math.radians(val1)))) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    # Cosine
    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))

        print("\nThe result is: " + str(math.tan((math.radians(val1)))) + "\n")

        # back to the main menu or exiting the program
        back = input("\nGo back to the main menu?, (y/n): ")

        if back == "y":
            continue
        else:
            break

    else:
        print("\n Invalid option \n")
        continue

