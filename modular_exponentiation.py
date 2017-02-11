# Finds the remainder of a power when divided by an integer

from base_b_expansion import expansion

def mod_exp(b, n, m):
    """
    b: an integer
    n: an integer
    m: a positive integer
    
    Returns the remainder when b^n is divided by m
    """
    
    n = expansion(n, 2)
    n.reverse()
    k = len(n)
    x = 1
    power = b % m
    
    for i in range(k):
        if n[i] == 1:
            x = (x * power) % m
        power = (power * power) % m
    
    return x
    
print(mod_exp(3, 644, 645))
