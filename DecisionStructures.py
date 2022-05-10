#Placing the hash tag in front of a line will make the line not execute 
#This is referred to as a "comment" 

'''
Line 1 of block comment 
Line 2 of block comment 
Line 3 of block comment 
*single quotation* 
''' 

"""
Line 1 of block comment 
Line 2 of block comment 
Line 3 of block comment 
*double quotation*
""" 

"""
A condition is a comparison. 
Conditions evaluate a boolean to be true or false.
If a condition is true, the following block of code will run.
A block of code will be indented. 

COMPARISONS: 
>    Greater than 
<    Less than 
>=    Greater than or equal to
<=    Less than or equal to
==    Equal to 
!=    Not equal to

""" 

mark = int(input("Please enter your test mark:"))
    

if mark >= 90:
    print("You aced it!")
    
elif mark >= 70:
    print("You got a B! Good job!")
    
elif mark >= 60:
    print("That'd s C!")
    
elif mark >= 50:
    print("You barley made it!")
    
else:
    print("You failed!")
    
if (mark >= 0 and mark <= 100):
    print("You have a valid mark")
    
if (mark > 100 or mark <0):
    print("This is an invalid mark")


"""
elif = if the condition above wasn't met, it'll execute the next one

else = if all the condition above wasn't met, it'll execute this one

and = both the conditions need to be met 

or = either one of the conditions need to be met 

""" 
