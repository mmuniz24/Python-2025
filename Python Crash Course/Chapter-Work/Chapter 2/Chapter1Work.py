#First string
#To run the program, use the command: python Chapter1Work.py
#Make sure you are in the correct directory where the file is located.
print("Hello Python World!")

##Variables
#using a variable to store a string
message = "This is the hello world message stored in a variable."
print(message)

message = "This is a new message that replaces the old one."
print(message)

#Make sure to save the file after making changes. changes wont reflect
#until the file is saved.

##Naming and Using Variables
message = "Error message on purpose."
print(message)

##Strings
#You can use "" or '' to create strings in Python.

name = "ada lovelace"
print(name.title())  #Title Case

name = "Ada Lovelace"
print(name.upper())  #Upper Case 
print(name.lower())  #Lower Case

##Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
#this is called an f-string, f = "format"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

##Adding Whitespace to Strings with Tabs or Newlines

example = "Python"
exampleWithTab = "\tPython"
exampleWithNewLine = "Languages:\nPython\nC\nJavaScript"
print(example)
print(exampleWithTab)
print(exampleWithNewLine)

exampleWithMoreNewLines = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(exampleWithMoreNewLines)

favorite_language = '   python  '
print(favorite_language)
print(favorite_language.rstrip())  #removes whitespace on the right side
print(favorite_language.lstrip())  #removes whitespace on the left side
print(favorite_language.strip())   #removes whitespace on both sides

##Removing prefixes
favorite_language = 'python'

url = 'https://www.example.com'
print(url.removeprefix('https://'))

##Numbers

print(2 + 3)
print(5 - 2)
print(4 * 3)
print(16 / 2)
print(3 ** 2)  #Exponentiation
print(7 // 3)  #Floor Division
print(7 % 3)   #Modulus
print(0.1 + 0.2)  #Floating Point Addition

#When you mix integers and floating-point numbers in an operation
#it will always result in a floating-point number.
print(3 + 2.0)  #Results in 5.0

##Multiple assignments
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

##Constants
PI = 3.14159
print(PI)

##Zen of Python
import this
#The Zen of Python is a collection of guiding principles for writing computer programs in the Python programming language.
#To read more about The Zen of Python, you can visit: https://peps.python.org/pep-0020/

