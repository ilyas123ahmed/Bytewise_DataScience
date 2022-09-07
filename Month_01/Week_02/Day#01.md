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

| Operator	| Name	         |Example	|
| ---       | ---            |  ---   |   
|+	       | Addition	       | x + y	|
|-	       |Subtraction	     | x - y	|
|*	       |Multiplication	 |   x * y|	
|/	       |Division	       |   x / y|	
|%	       |Modulus	         | x % y	|
|**	     |Exponentiation	   | x ** y	|
|//	     |Floor division	   | x //y  |


# Assignment Operators
Assignment operators are used to assign values to variables:

|Operator  	|Example         |	Same As|	
| ---       | ---            |  ---   | 
| =	        | x = 5	         |  x = 5	|
| +=	      |  x += 3	       |  x = x + 3	|
| -=	      |  x -= 3	       |  x = x - 3	|
| *=	      |  x *= 3	       |  x = x * 3	|
| /=        | 	x /= 3	     |  x = x / 3	|
| %=	      |  x %= 3	       |  x = x % 3	|
| //=	      |  x //= 3	     |  x = x // 3	|
| **=	     |   x **= 3	     |  x = x ** 3	|
| &=	     |   x &= 3	       |  x = x & 3	 |
| |=	     |   x |= 3	       |  x = x | 3	|
| ^=	     |   x ^= 3	       |  x = x ^ 3	|
| >>=	     |   x >>= 3	     |  x = x >> 3	|
| <<=	     |   x <<= 3	     |  x = x << 3  |


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
The following table lists all operators from highest precedence to lowest.

Operator	Description
**	Exponentiation (raise to the power)
~ + -	Complement, unary plus and minus (method names for the last two are +@ and -@)
* / % //	Multiply, divide, modulo and floor division
+ -	Addition and subtraction
>> <<	Right and left bitwise shift
&	Bitwise 'AND'td>
^ |	Bitwise exclusive `OR' and regular `OR'
<= < > >=	Comparison operators
<> == !=	Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators



# Comparison Operators 
Comparison operators are used to compare two values:

|Operator   |	 Name                    |	Example|	
|---        |---                       |---      |
|==	        | Equal                    | x == y | 	
|!=	        | Not equal                |x != y   |	
|>	        |Greater than	             |x > y    |	
|<	        |Less than	               |x < y	   |
|>=	        |Greater than or equal to	 |x >= y   |	
|<=	        |Less than or equal to     |x <= y   |


# Logical Operators
Logical operators are used to combine conditional statements:

|Operator	|  Description	                                              |Example|	
|---      |  ---                                                        | ---   |
|and 	    |  Returns True if both statements are true	                  |   x < 5 and  x < 10	|
|or	      |  Returns True if one of the statements is true              |	x < 5 or x < 4	|
|not	      |  Reverse the result, returns False if the result is true    |	not(x < 5 and x < 10)|

# If Statements
Python supports the usual logical conditions from mathematics:

- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b
- These conditions can be used in several ways, most commonly in "if statements" and loops.

### Example
An "if statement" is written by using the if keyword.
```pyhton
a = 33
b = 200
if b > a:
  print("b is greater than a")
```  

# While Loops
Python has two primitive loop commands:
- while loop
- for loop
With the while loop we can execute a set of statements as long as a condition is true.

### Example
Print i as long as i is less than 6:
```pyhton
i = 1
while i < 6:
  print(i)
  i += 1
```

### Example
Exit the loop when i is 3:
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

# For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

### Example
Print each fruit in a fruit list:
```pyhton
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

### Example
Exit the loop when x is "banana", but this time the break comes before the print:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```

# Lists
Lists are used to store multiple items in a single variable.Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

- Lists are created using square brackets:

- List Items
List items are ordered, changeable, and allow duplicate values.List items are indexed, the first item has index [0], the second item has index [1] etc.

- Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.If you add new items to a list, the new items will be placed at the end of the list.

- Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

- Allow Duplicates
Since lists are indexed, lists can have items with the same value:
```python
 thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```
# List Methods
Python has a set of built-in methods that you can use on lists.

### Method	Description
- append()	Adds an element at the end of the list
- clear()	Removes all the elements from the list
- copy()	Returns a copy of the list
- count()	Returns the number of elements with the specified value
- extend()	Add the elements of a list (or any iterable), to the end of the current list
- index()	Returns the index of the first element with the specified value
- insert()	Adds an element at the specified position
- pop()	Removes the element at the specified position
- remove()	Removes the item with the specified value
- reverse()	Reverses the order of the list
- sort()	Sorts the list

# The range() Function 
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

### Syntax
range(start, stop, step)

Parameter Values
Parameter	Description
- start	Optional. An integer number specifying at which position to start. Default is 0
- stop	Required. An integer number specifying at which position to stop (not included).
- step	Optional. An integer number specifying the incrementation. Default is 1

### Example
 Create a sequence of numbers from 3 to 5, and print each item in the sequence:
```python
x = range(3, 6)
for n in x:
  print(n)
```



# Tuples
Tuples are used to store multiple items in a single variable.Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.
- Tuple items are ordered, unchangeable, and allow duplicate values.
- Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
- Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
- Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
- Allow Duplicates
Since tuples are indexed, they can have items with the same value:

### Example
Tuples allow duplicate values:
```python
 thistuple = ("apple", "banana", "cherry", "apple", "cherry")
 print(thistuple)
```


