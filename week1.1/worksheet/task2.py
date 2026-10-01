"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: LIU JINGLEI
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try:
    save = input("Please enter a number about the amount of monthly saving: ")
    # Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
    total = int(int(save)*12)
    # print this out for the user with a suitable message.
    print("You will save " + str(total) +"in a year!!")
 # Validate that they have entered an integer.
except ValueError:
    print("The number weis not a integer")





# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

