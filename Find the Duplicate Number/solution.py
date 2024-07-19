
def findDuplicate(nums) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    temp_obj = {}
    
    for n in nums:
        if n in temp_obj:
            return True
        temp_obj[n] = 1
        
    return False


print(findDuplicate([3,1,3,4,2])) # True
print(findDuplicate([1,3,4,2])) # False
