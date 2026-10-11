# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)


    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        ret = max(self.height(node.right), self.height(node.left)) + 1
        return ret

        