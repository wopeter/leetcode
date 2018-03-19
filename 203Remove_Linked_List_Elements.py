"""
Description
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

"""
#Definition for singly-linked list.
#class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtypr: ListNode
    """
    
    if not head:
        return head
    pre, head = head, head.next
    while cur:
        if cur.val == val:
            pre.next = cur.next
            cur = cur.next
        else:
            pre = cur
            cur = cur.next
    return head if head.val !=val else head.next
    
    
    def myRemoveElements(self, head, val):
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        reHead = head
        if not head:
            return None
        pre, cur = head, head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.cur.next
            else:
                pre, cur = cur, cur.next
        return reHead