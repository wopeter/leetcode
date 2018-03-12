'''
Given an array of integers, every element appears twice except for one. Find
that singe one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

'''

'''
Concept 
1.if we take XOR of zero and some bit, it will return that bit: a XOR 0 = a
2.if we take XOR of two some bits, it will return 0: a XOR a = 0
3.a XOR b XOR a = (a XOR a) XOR b = 0  OXR b = b
'''

class Solution(object):
    '''
    :type nums: List[int]
    :rtype: int
    '''
    a = 0
    for i in nums:
        a ^= i
    return a