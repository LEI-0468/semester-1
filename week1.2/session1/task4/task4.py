# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
# print: tomato
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# food = union of fruit and vegetables so it will print all the item of them
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("banana")
print(fruit)
# Remove an item from vegetables
vegetables.remove("tomato")
# Find and display symmetric difference of the two sets
smd = fruit.symmetric_difference(vegetables)
print(smd)