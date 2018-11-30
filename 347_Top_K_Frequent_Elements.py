"""
Descriptioon
347.Top K Frequent Elements
Given a non_empty array of integers, return the k most frequent elements.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from colletions import Counter
        c = Counter(nums)
        res = [i[0] for i in c]
        return res
        
    def topKFrequent(self, nums, k):
        from colletions import Counter
        return list(zip(*Counter(nums)))[0]
        
        