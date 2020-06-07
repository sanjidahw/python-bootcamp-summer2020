subtotal = 0
# user_done = False
while True:
    user_selection = int(input("What is your selection? "))
    if user_selection == 1:

        print("You chose waffle cone")
        subtotal += 3.99
        flavor = int(input("What flavor do you want?"))
        if flavor == 1:
            print("you chose chocolate")
            subtotal += 0.50
        elif flavor == 2:
            print("you chose vanilla")
            subtotal += 0.50
        elif flavor == 3:
            print("you chose strawberry")
            subtotal += 0.50
        elif flavor == 4:
            print("you chose Rocky Road")
            subtotal += 0.75
        elif flavor == 5:
            print("you chose Cookie Dough")
            subtotal += 0.75
        else:
            print("You're eating a raw cone")

    elif user_selection == 2:
        print("You chose cup")
        subtotal += 2.99
        flavor = int(input("What flavor do you want?"))
        if flavor == 1:
            print("you chose chocolate")
            subtotal += 0.50
        elif flavor == 2:
            print("you chose vanilla")
            subtotal += 0.50
        elif flavor == 3:
            print("you chose strawberry")
            subtotal += 0.50
        elif flavor == 4:
            print("you chose Rocky Road")
            subtotal += 0.75
        elif flavor == 5:
            print("you chose Cookie Dough")
            subtotal += 0.75
        else:
            print("You're eating a raw cup")

    elif user_selection == 3:
        print("You chose regular cone")
        subtotal += 1.99
        flavor = int(input("What flavor do you want?"))
        if flavor == 1:
            print("you chose chocolate")
            subtotal += 0.50
        elif flavor == 2:
            print("you chose vanilla")
            subtotal += 0.50
        elif flavor == 3:
            print("you chose strawberry")
            subtotal += 0.50
        elif flavor == 4:
            print("you chose Rocky Road")
            subtotal += 0.75
        elif flavor == 5:
            print("you chose Cookie Dough")
            subtotal += 0.75
        else:
            print("You're eating a raw cup")

    elif user_selection == 4:
        print("Thank you for shopping with us today")
        break

    else:
        print("Invalid option -- please pick again!")

print(f"Your subtotal is: ${subtotal}")

sales_tax = 0.08875 * subtotal
print(f"Your taxes is: ${sales_tax}")

total = subtotal + sales_tax
print(f"Your total amount is: ${total}")
