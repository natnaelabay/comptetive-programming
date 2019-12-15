# Natnael Abay

# se.natnael.abay@gmail.com

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def innerFunction(root):
            if root:
                innerFunction(root.left)
                innerFunction(root.right)
                answer.append(root.val)
        
        answer = []
        innerFunction(root)
        return answer
