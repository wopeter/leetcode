"""
Description

Write a function that takes an unsigned integer and returns the number of '1' bits it has.
For example, the 32-bit integer '11' has binary representation 000000000000...001011, so the function should return 3.

solution2:
n represent as:     [... 1 1 0 1 0 0]
n - 1 represent as: [... 1 1 0 0 1 1]
In the binary representation, the least significant 1-bit in n always corresponds to a 0-bit in n - 1.
Therefore, annding two numbers n and n - 1 always flips the least significant 1-bit in n to 0, and keeps all 
other bits the same.

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
    
    #solution2 when n is [1 0 0 0 0 ....], this solution only calculate once, 
    def hammingWeight2(self, n)
        int sum = 0
        while n:
            sum += 1
            n &= (n - 1)
        return sum