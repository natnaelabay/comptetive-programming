# Natnael Abay

# se.natnael.abay@gmail.com


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None



class Solution:
    def reverseList(self, head):  # Iterative
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr =  next
        return prev
