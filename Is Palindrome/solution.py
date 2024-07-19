def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    s = ''.join(e for e in s if e.isalnum())
    
    right_index = len(s) - 1
    left_index = 0
    
    while left_index < right_index:
        if s[right_index].lower() != s[left_index].lower():
            return False
        left_index += 1
        right_index -= 1
    
    return True



print(isPalindrome("A man, a plan, a canal: Panama")) # True      
print(isPalindrome(" ")) # True   
print(isPalindrome("race a car")) # False   
