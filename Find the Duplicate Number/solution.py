
def findDuplicate(nums) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    temp_arr = []
    
    biggest_num = 0

    for n in nums:
        if n > biggest_num:
            biggest_num = n
    
    for n in range(biggest_num+1):
        temp_arr.append(0)
    
    for n in nums:
        temp_arr[n] += 1

    for n in  temp_arr:
        if n > 1 :
            return True
        
    return False


print(findDuplicate([3,1,3,4,2])) # True
print(findDuplicate([1,3,4,2])) # False
