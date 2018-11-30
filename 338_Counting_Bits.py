"""
Description
338. Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [None] * (num+1)
        
        res[0] = 0
        for n in range(1, num+1):
            temp = n ^ (n-1)
            if temp >= n:
                res[n] = 1
            else:
                res[n] = res[n-1] - res[temp] + 2
        return res
        
    def countBits2(self, num):
        dp = [0] * (num + 1)
        for i in range(1, num+1):
            dp[i] = dp[i>>1] + (i & 1)
        return dp
    