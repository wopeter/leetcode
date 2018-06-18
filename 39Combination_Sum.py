"""
NO 39. Combination Sum

Description
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

"""

class Solution():
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.resList
    
    def dfs(self, candidates, subList, target, last):
        if target == 0:
            self.resList.append(subList[:])
        if target < candidates[0]:
            return
        for n in candidates:
            if n > target:
                return
            if n < last:
                continue
            subList.append(n)
            self.dfs(candidates, subList, target-n, n)
            subList.pop()
            
    def combinationSum2(self, candidates, target):
        result = []
        
        def dfs(index, temp_solution, temp_sum):
            if temp_sum == target:
                result.append(temp_solution[:])
                return
            for i in range(index, len(candidates)):
                if temp_sum + candidates[i] <= target:
                    temp_solution.append(candidates[i])
                    dfs(i, temp_solution, temp_sum+candidates[i])
                    temp_solution.pop()
        if candidates:
            dfs(0, [], 0)
        return result