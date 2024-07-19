
def twoSum(nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        num_to_index = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            
            if diff in num_to_index:
                return [num_to_index[diff], index]
            
            num_to_index[num] = index              
        
    

print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSum([3,3], 6)) # [0,1]