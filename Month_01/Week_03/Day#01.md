# PYTHON MODULES AND PACKAGES


## Modules
Any Python file with a .py extension is a Module in Python.
A Python module is any Python files with a .py extension. It can be imported into python without the .py part.
A modules grants us reusability.
A module’s contents are accessed with the import statement.

```python
def multiply(x,y):
    result = x * y
    print(result)
```

Above code is contained in a file  called multiplication.py is called module.
we use this file by importing with 'import' keyword
And we can access the function called multiply with dot(.) operator.
```pyhton
import multiplication
multiplication.multiply(3,3)
```
### Output
```pyhton
9
```

When we work on big projects, it’s not a good practice to have all you python code in one single python file (.py).
That's why we splitting our code in different classes, functions and variables thoughtfully in separate python files (.py files) called modules.
Python allows you to import code in one module for use in other modules.

## Packages
Any Python file with a .py extension is a Module in Python.A python package is a collection of such modules along with a __init__.py file.
A Python package is nothing but a collection of modules along with a __init__.py file. The modules can also be arranged in hierarchy of folders inside a package.
We can import modules from packages using the dot (.) operator.
