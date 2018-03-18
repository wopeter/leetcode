"""
Description

Write a function that takes an unsigned integer and returns the number of '1' bits it has.
For example, the 32-bit integer '11' has binary representation 000000000000...001011, so the function should return 3.
"""


class Solution(object):
    def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count