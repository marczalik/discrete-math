# Adds the binary expansions of 2 integers

def bin_add(a, b):
    """
    a: a list, the binary expansion of an integer
    b: a list, the binary expansion of an integer
    
    Returns a list of the digits in the binary expansion of the sum of 2 integers.
    """
    
    a.reverse()
    b.reverse()
    
    if len(a) != len(b):
        if len(a) > len(b):
            len_diff = len(a) - len(b)
            for i in range(len_diff):
                b.append(0)
        if len(b) > len(a):
            len_diff = len(b) - len(a)
            for i in range(len_diff):
                a.append(0)
        
    
    n = len(b)
    c = 0
    s = [0] * len(b)
    
    for j in range(0, n):
        d = (a[j] + b[j] + c) // 2
        s[j] = a[j] + b[j] + c - 2 * d
        c = d
    
    s.append(c)
    s.reverse()
    
    return s

#~ print(bin_add([1, 1, 1, 0], [1, 0, 1, 1]))
