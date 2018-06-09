"""
No.19 Remove Nth Node From End of List

Description
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
class Solution:
	def def removeNthFromEnd(self, head, n):
		"""
		:typt head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		lengthOfList = 0
		point = head
		while point:
			lengthOfList += 1
			point = point.next
		offset = lengthOfList - n
		if offset == 0:
			return head.next
		point = head
		while offset > 1:
			point = point.next
			offset -= 1
		point.next = point.next.next
		return head