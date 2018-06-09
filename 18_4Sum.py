"""
No.18 Sum
Description

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.
Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,    0, 0, 1],
  [-2, -1, 1, 2],
  [-2,    0, 0, 2]
]

"""
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) -2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = len(nums) -1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right] - target
                    if temp > 0:
                        right -= 1
                    elif temp < 0:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left + 1 < right and nums[left+1] == nums[left]:
                            left += 1
                        while left < right - and  nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
    
    def fourSum2(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + sum(nums[-3:]) < target:
                continue
            if sum(nums[i:i+4]) > target:
                return res
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + sum(nums[j:j+3]) > target:
                    break
                if nums[i] + nums[j] + sum(nums[-2:]) < target:
                    continue
                left = j + 1
                right = len(nums) -1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right] - target
                    if temp > 0:
                        right -= 1
                    elif temp < 0:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left+1 < right and nums[left+1] == nums[left]:
                            left += 1
                        while right-1 > left and nums[right-1] == nums[right]:
                            right -= 1
                        left, right = left + 1, right -1
        return res
            
            
            
            
            
