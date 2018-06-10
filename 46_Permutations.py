"""
No.46 Permutations

Description:
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    #solution 1
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path+[nums[i]], res)
    
    #solution 2
    def permute2(self, nums):
        import itertools
        return list(itertools.permutations(nums))
        
    #solution 3   
    def permute3(self, nums):
        self.res = []
        self.dfs(nums, 0, len(nums)-1)
        return self.res
    def dfs(self, nums, k, m):
        if k == m:
            self.res.append(nums[:])
        else:
            for i in range(k, m+1):
                nums[i], nums[k] = nums[k], nums[i]
                self.dfs(nums, k+1, m)
                nums[i], nums[k] = nums[k], nums[i]
           
    