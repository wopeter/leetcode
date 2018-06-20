"""
No 55.Jump Game

Description

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n);
            if nums[i] == 0:
                if i == 0 and n > 1:
                    return False
                if i == 0 and n == 1:
                    return True
                if i == n - 1:
                    return True
                index = i
                while index - 1 >= 0:
                    if index - 1 == 0 and nums[index-1] <= i - index + 1:
                        return False
                    if nums[index-1] > i - index + 1:
                        break
                    else:
                        index -= 1
       return True  

    def canJump2(self, nums):
        n = len(nums)
        can = True
        smallest_idx = n - 1
        for i in range(n-2, -1, -1):
            can = i + nums[i] >= smallest_idx
            if can:
                smallest_idx = i
        return can
    def canJump3(self, nums):
        n = len(nums)
        lastPos = n - 1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0