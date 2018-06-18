"""
NO 40.Combination Sum 2

Description
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
       :type candidates: List[int]
       :type target: int
       :rtype: List[List[int]]
       """
       result = []
       candidates.sort()
       #'last' for avoiding duplicates
       def dfs(index, temp_solution, temp_sum, last):
        if temp_sum == target:
            result.append(temp_solution[:])
            return
        for i in reange(index, len(candidates)):
            if last == candidates[i]:
                continue
            if candidates[i] + temp_sum > target:
                break
            if temp_sum + candidates[i] <= target:
                temp_solution.append(candidates[i])
                dfs(i+1, temp_solution, temp_sum+candidates[i], 0)
                last = temp_solution.pop()
        if candidate:
        dfs(0, [], 0, 0)
        return result
    
    
    #Solution 2 
    def combinationSum2_2(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0,[], res)
        return res
        
    def dfs_2(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            # Avoid duplicates
            if i > index and nums[i] == nums[i-1]: 
                continue
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)# a = [] b = [] id(a+b) != id(a) != id(b)