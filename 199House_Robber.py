"""
Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

nums:      a1, a2, a3, ... a(n-2), a(n-1), a(n)
maxMoney:  a1, max(a1, a2), ...maxMoney[n-1], maxMoney[n]...
for every element of nums either included or not included if a(n) is included, then a(n-1) is not included.
In this case, maxMoney[n] = a(n) + maxMoney[n-2]
if a[n] is not included , in this case , maxMoney[n] = maxMoney[n-1]
so maxMoney[n] = max(maxMoney[n-1], a[n] + maxMoney[n-2])

"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, cur = 0, 0
        for n in nums:
            pre, cur = cur, max(pre + n, cur)
        return cur
        
    #My solution is more complex, but the idea is the same.
    def myRob(self, nums):
       # sum(n) = max(sum(n - 1), nums[n] + sum(n - 2))
        l = len(nums)
        maxMoney = 0
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0], nums[1])
        else:
            a = nums[0]
            b = max(nums[0], nums[1])
            for num in nums[2:]:
                maxMoney = max(b, num + a)
                a, b = b, maxMoney
        return maxMoney 