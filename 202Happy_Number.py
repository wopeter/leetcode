"""
Description
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        historySum = []
        squareSumNum = 0
        n0 = 0
        while squareSumNum != 1:
            squareSumNum = 0
            if n in historySum:
                return False
            else:
                historySum.append(n)
            while n != 0:
                n0 = n % 10
                squareSumNum = n0 ** 2 
                n //= 10
            n = squareSumNum
            
        return True 
            
            
            
            
            