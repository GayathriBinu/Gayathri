animals = ["Bird", "Fox", "Cat", "Rat", "Alligator"]

animals.append("Giraffe") 

moreAnimals = ["monkey", "ant eater", "red panda"]

animals.extend(moreAnimals)

animals.insert(4, "snake")

animals.pop(3)

animals.remove("snake")

del animals[2]

#deletes entire list
#del animals

for counter in animals:
    print(counter)
