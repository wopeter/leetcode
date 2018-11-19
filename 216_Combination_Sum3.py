"""
Description
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n:int
        :rtype: List[List[int]]
        """
        def combination(res, comb, k, start, n):
            if k == len(comb) and n == 0:
                res.append(comb[:])
                
            if k < len(comb) or n < 0:
                return
            for i in range(start, 10):
                comb.append(i)
                combination(res, comb, k, i+1, n-i)
                comb.pop(-1)
                
        res = []
        combination(res, [], k, 1, n)
        return res
        
    def combinationSum3_2(self, k, n):
        import itertools
        res = []
        combs = itertools.combination(list(range(1, 10)), k)
        for i in combs:
            if sum(i) == n:
                res.append(i)
        return res
        
        
        