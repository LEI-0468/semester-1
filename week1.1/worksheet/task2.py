"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: LIU JINGLEI
"""



# Ask the user to input an amount they want to save every month - this should be an integer.
try:
    name = input("What is your name? ")
    print(f"Welcome to LeedsBank's savings calculator {name}!")
    save = input("Please enter a number about the amount of monthly saving: ")
    # Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
    total = int(int(save)*12)
    # Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
    total += float(total*0.8)
    
    # print this out for the user with a suitable message.
    print("You will save £" +f"{total:.2f}"  + " in a year!!")
 # Validate that they have entered an integer.
except ValueError:
    print("The number weis not a integer")






# print this out in the format £X.XX (to two decimal places).

