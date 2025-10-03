""""
------------------------------------
PYTHON PRINT FUNCTION
------------------------------------
"""
print(" Hi \"Python\"")       # Escaping quotes
print("Yoo\n")                # New line
print("Mehhhh")
print("heloooo\nanyeonggg")   # Break line
print("kiyowooo\tkawaii")     # Tab space

# Challenge
"""  
-Use PRINT() to recreate this exact output, allowed to use only one PRINT()
Expected Output:
Your Learning Path: 
    - Python Basics
    - Data Engineering
    - AI
"""
# Solution
print("Your Learning Path:\n\t-Python Basics\n\t-Data Engineering\n\t-AI")

"""
------------------------------------
PYTHON VARIABLES
------------------------------------
"""
name = "Jemisha"
language = "Python"
print("My name is",name)
print(name,"is learning",language)
print(name,"wants to become",language,"expert")

# Challenge
"""  
-Print the following three lines
- add a variable to make it dynamic
Expected Output:
    info@datawithbaraa.com
    support@datawithbaraa.com
    www.datawithbaraa.com
"""
# Solution
email = "datawithbaraa.com"

print("info@" + email)
print("support@" + email)
print("www." + email)

# OR in one print with new lines
print("info@" + email, "\nsupport@" + email, "\nwww." + email)

"""
------------------------------------
PYTHON INPUT FUNCTIONS
------------------------------------
"""
name = input("Enter Your Name:")
country = "Germany"
print(name, "comes from", country)

"""
------------------------------------
PYTHON DATA TYPES
------------------------------------
"""
# Examples of Python Data Types
a = 10        # int
b = 3.15      # float
c = "Hello"   # str
d = 'Hi'      # str
e = "1234"    # str (not a number here)
f = True      # bool
g = False     # bool
h = None      # NoneType
i = ""        # str (empty string)
j = " "       # str (space character)

# Challenge
"""  
-Create 5 variables - each with a different data type:
    1. Your age
    2. Your height(with decimals)
    3. Your name
    4. Are you a student?
    5. Something with no value yet
Then print the values, data types, length of all variables
"""
# Solution
age = 20                # int
height = 164.6          # float
name = "Jemisha"        # str
student = True          # bool
hobby = None            # NoneType

print("Your age:", age, "| Data type:", type(age))
print("Your height:", height, "| Data type:", type(height))
print("Your name:", name, "| Data type:", type(name))
print("Are you a student?", student, "| Data type:", type(student))
print("Hobby:", hobby, "| Data type:", type(hobby))

print("\n--- Length of variables (if applicable) ---")
print("Length of name:", len(name))


