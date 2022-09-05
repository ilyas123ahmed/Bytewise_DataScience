# PYTHON BASICS 
# Your First Python Program
  print() can be used to output or dispaly any kind of text in the console window.This function will use to print our first program in python
  
  ```PYTHON
   print('I am ILYAS AHMED')
  ```
# Variables
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

## Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

```python
num = 5
name = "Ilyas"
print(num)
print(name)
```
In python we dont need to specify their type but If you want to specify the data type of a variable, this can be done with casting.
```python
 x = str(3)    # x will be '3'
 y = int(3)    # y will be 3
 z = float(3)  # z will be 3.0
```
## Many Values to Multiple Variables
 Python allows us to assign values to multiple variables in one line:
```python
 x, y, z = "Orange", "Banana", "Cherry"
 x = y = z = "Orange"

```

## Global and Local Variables 
Variables that are created outside of a function (as in all of the examples above) are known as global variables.Global variables can be used by everyone, both inside of functions and outside.



# Receiving Input

Python allows for user input.That means we are able to ask the user for input.we can take input from user or ask from user by input() function.
```python
 username = input("Enter username: ")
 print("Username is: " + username)
```

# Type Conversion
 There are 3 main data types in python:

- Numeric like 34 or 3.6
- Textual like 'D' or "ilyas"
- Boolean like True or False
They can be converted between each other in python. 
For example, an integer can be converted into a string like this,
```pyhton
 num = 34
 string = str(num)
 print(type(string))
```

```pyhton
 'str'
```
# Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

print("Hello")
print('Hello')


# Arithmetic Operators 
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	            Example	
+	       Addition	          x + y	
-	       Subtraction	      x - y	
*	       Multiplication	    x * y	
/	       Division	          x / y	
%	       Modulus	          x % y	
**	     Exponentiation	    x ** y	
//	     Floor division	    x // y


Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3


Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y


Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	Description	Example	Try it
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)



Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y


Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y



Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:


- Operator	  Name	                   Description
* & 	        AND	                     Sets each bit to 1 if both bits are 1
* |	          OR	                     Sets each bit to 1 if one of two bits is 1
* ^	          XOR	                     Sets each bit to 1 if only one of two bits is 1
* ~ 	        NOT	                     Inverts all the bits
* <<	        Zero                     fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
* >>	       Signed right shift	       Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


# Operator Precedence 
# Comparison Operators 
# Logical Operators
# If Statements
# Exercise
# While Loops
# Lists
# List Methods
# For Loops
# The range() Function 
# Tuples

