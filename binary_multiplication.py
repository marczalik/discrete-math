# Multiplies the binary expansions of 2 integers

from binary_addition import bin_add

def bin_multiply(a, b):
    """
    a: a list, the binary expansion of an integer
    b: a list, the binary expansion of an integer
    
    Returns a list of the digits in the binary expansion of the product of 2 integers
    """
    
    b.reverse()

    n = len(b)
    c = []
    
    for j in range(0, n):
        if b[j] == 1:
            temp_a = a[:]
            for x in range(j):
                temp_a.append(0)
            c.append(temp_a) 
        else:
            c.append([0])
    
    if n > 1:
        p = bin_add(c[0], c[1])
        for k in range(2, len(c)):
            p = bin_add(p, c[k])
    else:
        p = c[0]
    
    return p
    
print(bin_multiply([1, 1, 0, 0], [1, 0, 1, 1, 1]))
