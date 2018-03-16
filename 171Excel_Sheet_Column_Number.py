"""
Description
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = 0
        for num in s:
            temp = 26 * temp + ord(num) - ord('A') + 1
        return temp