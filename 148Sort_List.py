"""
Description

Sort a linked list in O(nlogn) time using constant sapce complexity
Input: 4->2->1->3
Output: 1->2->3->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l = []
        point = head
        while point:
            l.append(point.val)
            point = point.next
        l.sort()
        head = point = ListNode(0)
        for val in l:
            point.next = ListNode(val)
            point = point.next
        return head.next
        
        
        