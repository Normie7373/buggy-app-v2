
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
