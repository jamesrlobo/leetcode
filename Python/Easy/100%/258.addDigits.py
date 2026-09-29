def addDigits(num):
    """
    Repeatedly add all digits in a number until a single digit remains.
    
    Args:
        num: A non-negative integer
        
    Returns:
        int: A single digit (0-9) resulting from repeatedly summing all digits
        
    Examples:
        >>> addDigits(38)
        2
        >>> addDigits(0)
        0
    """
    while num > 9:
        num = (num%10) + (num//10)
    return num


num = 38
num = 0
num = 10
print(addDigits(num))
