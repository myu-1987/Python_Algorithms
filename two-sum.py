# Given an array of integers nums and an integer target, return 
# indices of the two numbers such that they add up to target.
class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        print(seen)
        return seen

        
        
            
    twoSum([2,7,11,15], 9)