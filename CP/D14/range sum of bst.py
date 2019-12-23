# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int, ans=0) -> int:
        #self.ans  = 0
        def traverese(root,L,R):
            if root:
                if root.val <= R and root.val >= L:
                    self.ans += root.val
                if root.left:
                    traverese(root.left,L,R)
                if root.right:
                    traverese(root.right,L,R)
        traverese(root,L,R)
        return self.ans