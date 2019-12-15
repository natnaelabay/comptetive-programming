# Natnael Abay

# se.natnael.abay@gmail.com

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        count = node
        while count.next.next:
            count.val = count.next.val
            count = count.next
        count.val = count.next.val
        count.next = None
        
    
        
