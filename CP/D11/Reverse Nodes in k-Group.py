# Natnael Abay

# se.natnael.abay@gmail.com

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        h = head
        t = head  
        leader = trailer = None        
        while t:
            for i in range(k - 1):               
                if not t:
                    break
                t = t.next        
            if not t:
                break
            trailer = t.next
            pre = leader
            cur = h
            #pre, cur = leader, h
            while cur != trailer:
                tmp = cur.next
                cur.next = pre
                pre, cur = cur, tmp
            if leader:
                leader.next = pre
            else:
                head = pre
            leader = h
            leader.next = trailer
            h = t = trailer
        return head
