def findMiddleIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = sum(nums)
    left = 0

    for a in range(len(nums)):
        right = total - left - nums[a]
        if right == left:
            return a
        left += nums[a]

    return -1  


print(findMiddleIndex([2,3,-1,8,4])) # 3
print(findMiddleIndex([1,-1,4])) # 2
print(findMiddleIndex([2,5])) # -1

