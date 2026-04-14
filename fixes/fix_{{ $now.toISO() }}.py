**ROOT CAUSE:** 
The error occurs because the `add_values` function in the `calculator.py` file is attempting to add an integer (`int`) and a string (`str`) together, which is not a supported operation in Python. This suggests that the function is receiving inputs of different data types than expected.

**FIX:**
To fix this issue, we need to ensure that both inputs to the `add_values` function are of the same numeric data type (either `int` or `float`). We can achieve this by adding input validation and type conversion to the function.

**CODE:**
```python
# app/utils/calculator.py

def add_values(a, b):
    """
    Adds two numeric values together.
    
    Args:
        a (int or float or str): The first value to add.
        b (int or float or str): The second value to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Raises:
        TypeError: If either a or b cannot be converted to a number.
    """
    # Attempt to convert inputs to float
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Both inputs must be numeric")
    
    # Now that inputs are validated and converted, we can safely add them
    return a + b
```
In this fixed version, we first attempt to convert both `a` and `b` to `float`. If either conversion fails (because the input is not a valid number), a `TypeError` is raised with a message indicating that both inputs must be numeric. If both conversions succeed, we then add the two numbers together and return the result. This approach ensures that the function can handle inputs that are either already numbers or can be converted to numbers (such as numeric strings), while also providing clear error messages for invalid inputs.