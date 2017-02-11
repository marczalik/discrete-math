# Calculates the greatest common divisor of 2 integers

def gcd(a, b):
    """
    a: positive integer
    b: positive integer
    
    Returns the greatest common divisor of a and b
    """
    
    x = a
    y = b
    
    while y != 0:
        r = x % y
        x = y
        y = r
    
    return x
    
print(gcd(414, 662))
