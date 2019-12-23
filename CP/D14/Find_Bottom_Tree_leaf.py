# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.depth = -1
        self.ans = 0
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.helper(root,0)
        return self.ans
    def helper(self,root,depth):
        if not root:
            return
        if depth >self.depth:
            self.ans = root.val
            self.depth = depth
        self.helper(root.left,depth+1)
        self.helper(root.right,depth+1)