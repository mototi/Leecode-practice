def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if len(s) != len(t):
        return False
    
    t_letters =  {}
    s_letters = {}
    
    for a in t:
        if a in t_letters:
            t_letters[a] += 1
        else:
            t_letters[a] = 1
    
    for a in s:
        if a in s_letters:
            s_letters[a] += 1
        else:
            s_letters[a] = 1
    
    for key in t_letters:
        if key not in s_letters or t_letters[key] != s_letters[key]:
            return False
    
    return t_letters == s_letters



print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))  # False

    