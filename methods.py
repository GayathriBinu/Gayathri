# Methods are blocks of code that are executed with a command
# Methods can be called anything, except keywords
# predefined Python methods 
# Methods are created at top of program in Python 
# Use the keyword "def" before the method 

#Method definition 
# THis method does not have any parameters 
def foo():
    # code to be executed when method is called
    print("Helo World!")
    print('potatoes')
    
# Beginning of Python program 
print("Welcome to my program.")
foo()

# THis method takes 2 parameters 
def bar(x,y):
    sum = x + y
    return sum
    
variable = bar(7,3) 
print(variable)
