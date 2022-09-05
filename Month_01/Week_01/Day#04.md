#  Topic #1: Hello, World! 

## What is python? 
Python is a cross-platform programming language, which means that it can run on multiple platforms like windows,macOS, and Linux, and has even been ported to the java and .net virtual machines.It is free and open-source. Even though most of today's Linux and mac have python pre-installed in it, the version might be out-of-date. So, it is always a good idea to install the most current version.

## How do you write hello world python?
 The easiest way to display anything on the output screen in the python programming screen is by using the print () function. To print hello world, we can design a python hello world program that will print “hello world” to theoutput screen using the print () function. It is very simple code to printsomething in python. Whatever we write in between single or double quotes in square brackets they print out.



# Topic #2: Variables and Types

 ## What are variables in python?
 Python is completely object-oriented, and not "statically typed". You do not need to declare variablesbefore using the or declaring their type. Every variable in Python is an object. 

Integer Numbers Integer_number = 7 Float Numbers Float_number = 7.0 String We can declare in
 single or double quotes String_ letters = “Hello” String_ letters = ’Ilyas’ Mixing operators
 between numbers and strings is not supported in python 



 # Topic #3: Lists What is the list?

 Lists are very similar to arrays. They can contain any type of variable,and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

### Example:
Names = ["John", "Eric", "Jessica"] 
my_list = [1, 2, 3, ‘a’, ‘b’] We can also declare a list of list.
MyList= [[1, 2, 3, 4], [12, 13, 23], [10, 20, 30], [11, 22, 33], [12, 24, 36]]

We can use the append () function to insert the elements in the list
my_list = [] my_list.append (1) 

We can change list item
`~`python
  thislist = ["apple", "banana", "cherry"]
  thislist[1] = "blackcurrant"
  print(thislist)
`~`
We can remove element from list 
`~`python
 thislist = ["apple", "banana", "cherry"]
 thislist.remove("banana") 
 print(thislist)
`~`
 We can also perform some of the following functions as well. 

clear() Removes all the elements from the list 
copy() Returns a copy of the list 
count() Returns the number of elements with the specified value 
extend() Add the elements of a list (or any iterable), to the end of the current list 
index() Returns the index of the first element with the specified value 
insert() Adds an element at the specified position pop() Removes the element at the specified position 
remove() Removes the first item with the specified value reverse() Reverses the order of the list 
sort() Sorts the list.
