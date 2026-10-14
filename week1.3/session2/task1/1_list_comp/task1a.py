# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)


# write the equivalent for loop to create the not_fish list from animals
for i in range (len(animals)-1):
    if animals[i] != 'goldfish' :   
        not_fish.append(animals[i])


print(not_fish) 
# print your result to verify it is the same