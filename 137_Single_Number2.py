"""
137. Single Number II
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) // 2
        
        
    def singleNumber2(self, nums):
        ans = 0
        for i in range(32):
            bit = 0
            for j in range(len(nums)):
                if ((nums[j] >> i) & 1) == 1:
                    bit += 1
                    bit %= 3
            if bit != 0:
                ans |= bit << i
        if ans >= 2 ** 31:
            ans -= 2 ** 32:
        return ans
        
        