"""
Description:
Given a positive integer, rturn its corresponding column title as appear in an excel sheet.
for example:
1 -> A
2 -> B
...
26 -> Z 
27 -> AA
...
"""




class Solution:

    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while num:
            ans = chr(ord('A') + (num - 1) % 26) + ans
            num = (num - 1) / 26
        return ans