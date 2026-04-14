
def add_values(a, b):
    """
    Adds two numeric values and returns the result.
    
    Args:
        a (int or float): The first value to add.
        b (int or float): The second value to add.
    
    Returns:
        int or float: The sum of a and b.
    
    Raises:
        TypeError: If a or b is not a numeric value.
    """
    # Check if a and b are numeric values
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both values must be numeric")
    
    # Attempt to add a and b
    return a + b
