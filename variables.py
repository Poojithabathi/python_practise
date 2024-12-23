# variables are used to store data values that can be accessed and manipulated throughout a program. 
# Variables act as containers or references for data. 
# Unlike some other programming languages, Python variables do not need to be explicitly declared with a data type. 
# Instead, the type of a variable is dynamically inferred based on the value assigned to it.


# 1) Dynamic Typing: Python is a dynamically typed language, which means that the type of a variable is inferred at runtime based on the value assigned to it. 
# example:
x = 5
print(x)
x = "hello"
print(x)



# 2) Variable Names: Variable names in Python can contain letters, numbers, and underscores, but they cannot start with a number.
# They are case-sensitive, which means that variables with different capitalization are considered different variables.
# Variable names should be descriptive and meaningful to make the code more readable and maintainable.
# It is also a good practice to use lowercase letters and underscores to separate words in variable names, following the snake_case naming convention.
# example:
first_name = "John"
last_name = "Doe"
age = 30
print(first_name, last_name, age)   # Output: John Doe 30


# 3) Case Sensitivity: Variable names in Python are case-sensitive, which means that variables with different capitalization are considered different variables.
# example:
x = 5
X = 10
print(x)    # Output: 5
print(X)    # Output: 10


# 4) Reserved Words: Python has a number of reserved words that cannot be used as variable names, as they have special meanings in the language.
# example:
# int = 5    # SyntaxError: invalid syntax
# print(int) # Output: <class 'int'>
# In this example, int is a reserved word in Python that is used to represent integer values.


# 5) Multiple Assignment: Python allows for multiple variables to be assigned in a single statement, which can be useful for swapping values between variables.
# example:
x, y, z = 5, 10, 15
print(x, y, z)  # Output: 5 10 15
x, y = y, x
print(x, y)     # Output: 10 5


# 6) Variable Scope: The scope of a variable refers to the region of a program where the variable can be accessed.
# In Python, variables can have global or local scope, depending on where they are defined.
# Global variables are defined outside of any function and can be accessed from anywhere in the program.
# Local variables are defined within a function and can only be accessed from within that function.
# example:
# Global variable
x = 5


# 7) Global Variables: Global variables are variables that are defined outside of any function and can be accessed from anywhere in the program.
# example:
x = 5
def print_x():
    print(x)
print_x()   # Output: 5
# In this example, the variable x is defined outside of any function, making it a global variable that can be accessed from within the print_x function.


# 8) Local Variables: Local variables are variables that are defined within a function and can only be accessed from within that function.
# example:
def print_x():
    x = 5
    print(x)
print_x()   # Output: 5
# In this example, the variable x is defined within the print_x function, making it a local variable that can only be accessed from within that function.


# 9) Constants: Constants are variables whose values should not be changed once they are assigned. In Python, there is no strict way to define constants, but naming conventions can be used to indicate that a variable should be treated as a constant.
# example:
PI = 3.14159
print(PI)   # Output: 3.14159
# In this example, the variable PI is named in all uppercase letters to indicate that it should be treated as a constant.


