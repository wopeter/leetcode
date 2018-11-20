"""
Description
238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        product = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
                
        if zeroCount >= 2:
            return [0] * len(nums)
            
        if zeroCount == 1:
            for num in nums:
                if num != 0:
                    res.append(0)
                else:
                    res.append(product)
            return res
            
        return list(map(lambda x: product // x, nums))
        
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        res[0] = 1
        for i in range(len(nums)):
            res[i] = res[i-1] * nums[i-1]
            
        right = 1
        for i in range(len(nums), -1, -1):
            res[i] = res[i] * right
            right = right * nums[i]
        return res
            
            