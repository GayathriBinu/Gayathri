#Import math module at top of program 
import math

# VARIABLE DEFINITON 

base = 0 
exponent = 0 
answer = 0 

base = int(input('Please enter a base: '))
exponent = int(input('Please enter an exponent: '))
 
answer = math.pow(base, exponent)

print(str(base) + " raised to " + str(exponent) + ' is ' + str(answer))

#math.floor rounds down a number 
