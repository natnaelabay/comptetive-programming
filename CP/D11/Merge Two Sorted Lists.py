# Natnael Abay

# se.natnael.abay@gmail.com



#Got a ittle help from my teacher

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        t = ListNode(0)
        dm = t
        while l1 and l2:
            if l1.val <l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        if l1:
            t.next = l1
        if l2:
            t.next = l2
        return dm.next
