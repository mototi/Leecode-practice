def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 1:
        return True
        
    power = 0 
    product_result = 1

    while product_result < n:
        product_result = 1
        i = 1
        while i <= power:
            product_result *= 2
            i += 1
        power += 1
    
    if product_result == n:
        return True
    else:
        return False 
    
print(isPowerOfTwo(33))