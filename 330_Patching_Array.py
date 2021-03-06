"""
330. Patching Array
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
"""

class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        added = i = 0
        while miss <= n:
            if (i < len(nums)) and (nums[i] < miss):
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added
"""
Explanation:
Let miss be the smallest sum in [0, n] that we might be missing. Meaning we already know we can build all sums
in [0, miss), Then if we have a number num <= miss in the given array, we can add it to those smaller sums to build all sums in [0, miss+num).If we don't, then we must add such a number to the array, and it's best to add
miss itself, to maximize the reach.
"""     
    def minPatches2(self, nums, n):
        sum = ans = i = 0
        while sum < n:
            if (i < len(nums) and nums[i] <= sum + 1):
                sum += nums[i]
                i += 1
            else:
                ans += 1
                sum += sum + 1
        return ans
        
 


