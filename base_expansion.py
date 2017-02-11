# Converts an integer from one base to another

def expansion(n, b):
    """
    n: a positive integer
    b: an integer greater than 1
    
    Returns a list of digits corresponding to the base b expansion of n
    """
    
    a = []
    q = n
    
    while q != 0:
        a.append(q % b)
        q = q // b
    
    a.reverse()
     
    return a
        
print(expansion(42, 2))
