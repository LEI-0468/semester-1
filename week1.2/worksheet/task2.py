# Worksheet 1.2: Task 2 Solution
def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers
import sys
nums = []
print("please enter a sequence of float values")
from util import read_numbers
nums = read_numbers()

if (len(nums)==0): sys.exit("Error: no numbers provided")
nums.sort()
print(f"Minimum = {nums[0]}")

print(f"Maximum = {nums[len(nums)-1]}")


mean =float(0)
mean = sum(nums)/len(nums)
print(f"Mean = {mean}")


if (len(nums)%2 == 1) :
    print(f"Median = {nums[int(len(nums)/2)]}")
else : 
    print(f"Median = {(nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2}")##int(len(nums)/2)]+nums[int(len(nums)/2+1)])/2