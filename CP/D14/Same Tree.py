# Natnael Abay

# se.natnael.abay@gmail.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if q is None and p is None:
            return True
        elif q is None:
            return False
        elif p is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left,q.left)
            
