# Worksheet 1.2: Task 1 Solution
import sys
try:
    num = int(input ("Please enter an intenger between 1 to 100:"))
    if (num < 0 ): sys.exit("Error: Grade must be an integer between 0 and 100") 
    if (num > 100) : sys.exit("Error: Grade must be an integer between 0 and 100") 
    if (num < 40) : print( f"{num} is a Fail")
    if (num < 70 and num > 39) : print( f"{num} is a Pass")
    if (num < 101 and num > 69) : print( f"{num} is a Distinction")
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100")