Basic Python Tasks. (Hackerrank) 

## Task 1:Loops

### Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

Sample Input 
``` python
  5
 ```
Sample Output 
```python
0
1
4
9
16
```

### Code 
```python
if __name__ == '__main__':
     n = int(input())
for i in range(0,n):
   print(i**2) 
```
My Input 
``` python
  5
 ```
My Output 
```python
0
1
4
9
16
```

## Task 2: Functions

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

### Task

- Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

- Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

- The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 
```python
1990
```
Sample Output 
```python
False
```

### Code
```pyhton
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 400 == 0 :
        leap = True
    elif year % 100 == 0:
       leap = False 
    elif year % 4 == 0 :
        leap = True  
    
    return leap

year = int(input())

```
My Input 
```python
1990
```
My Output 
```python
False
```
