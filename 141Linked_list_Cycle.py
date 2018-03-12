'''
Description:
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
快慢指针技巧，slow指针和fast指针开始同时指向头结点head， fast每次走两步， slow每次走一步。如果链表不存在环，
那么fast或者fast.next会先到None
。如果链表中存在环路，则由于fast指针移动的速度是slow指针的速度的两倍， 所以在进入环路以后，俩个指针迟早会相遇，
如有一时刻slow==fast，则说明存在环路

'''
'''
逐步判断每个节点，并将判断过的结点的next指向head， 若当前判断的结点指向之前的某一结点，该结点的next又指向了
head结点通过cur.next == head?可以判断其是否是环路，否则返回False
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
            return True
        return False
        
    def hasCyle2(self, head):
        cur = head
        while cur:
            if cur.next == head:
                return True
            n = cur.next
            cur.next = head
            cur = next
        return False