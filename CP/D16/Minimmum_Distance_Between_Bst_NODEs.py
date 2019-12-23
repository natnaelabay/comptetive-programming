# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.arr = []
        if root:
            self.inorder(root)
        least = 99999
        arr = sorted(self.arr)
        for i in range(0,len(arr)-1):
            if arr[i+1]-arr[i] < least:
                least = arr[i+1] - arr[i]
            
        return least
            
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        self.arr.append(root.val)
        if root.right:
            self.inorder(root.right)c