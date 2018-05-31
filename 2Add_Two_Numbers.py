'''
2.Add Two Numbers
Description:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        point = head
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = temp // 10
            temp = temp % 10
            point.next = ListNode(temp)
            point = point.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp = l1.val + carry
            carry = temp // 10
            temp = temp % 10
            point.next = ListNode(temp)
            point = point.next
            l1 = l1.next
        while l2:
            temp = l2.val + carry
            carry = temp // 10
            temp = temp % 10
            point.next = ListNode(temp)
            point = point.next
            l2 = l2.next
        if carry != 0:
            point.next = ListNode(carry)
        return head.next
		
		def Solution2(self, l1, l2):
			carry = 0
			headNode = preNode = ListNode(0)
			while l1 or l2 or carry:
				if l1:
					carry += l1.val
					l2 = l2.next
				if l2:
					carry += l2.val
					l2 = l2.next
				carry, val = divmod(carry, 10)
				preNode.next = ListNode(val)
				preNode = preNode.next
			return headNode.next
		
		