# Natnael Abay

# se.natnael.abay@gmail.com

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        cur = head.next
        pre = head
        while cur:
            if cur.val==pre.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = pre.next
        return head
        
