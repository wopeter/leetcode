"""
NO 47.Permutations 2

Description
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        def helper(nums, point):
            if point == n - 1:
                res.append(nums[:])
                return
            for i in range(point, n):
                if i > point and nums[i] == nums[i-1]:
                    continue
                nums[point], nums[i] = nums[i], nums[point]
                index = i-1
                while index-1 > point and nums[index] < nums[index-1]:
                    nums[index], nums[index-1] = nums[index-1], nums[index]
                    index -= 1
                helper(nums, point+1)
                while index < i:
                    nums[index+1], nums[index] = nums[index], nums[index+1]
                    index += 1
                nums[point], nums[i] = nums[i], nums[point]
        helper(nums, 0)
        return res
