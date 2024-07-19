def arrayStringsAreEqual(word1, word2):
    """
    :type word1: List[str]
    :type word2: List[str]
    :rtype: bool
    """

    word1 = "".join(word1)
    word2 = "".join(word2)
    
    if word1 == word2:
        return True
    
    return False


print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))  # True
print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))  # False
print(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])) #True
