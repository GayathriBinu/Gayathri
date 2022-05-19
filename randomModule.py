# The see() method is used to initialize the random num gen
# Need a number to start (start value) to generate a random num
# By default, it will use the system clock 
# Use the seed() method to customize the start number of the random num gen

import random 

#random.seed(13)
print(random.random())

#random.seed(1444)
print(random.random())

print(random.randint(1, 100))
