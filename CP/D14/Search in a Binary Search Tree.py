# Natnael Abay

# se.natnael.abay@gmail.com

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val >val:
                cur = cur.left
            elif cur.val < val:
                cur = cur.right
        return 
