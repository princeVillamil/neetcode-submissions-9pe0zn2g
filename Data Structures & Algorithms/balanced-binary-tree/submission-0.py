# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True
        def dfs(root):
            nonlocal isBal
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            print(left + right)
            if (max(left, right) - min(left,right)) > 1: isBal = False

            return 1 + max(left, right)
        
        dfs(root)
        return isBal