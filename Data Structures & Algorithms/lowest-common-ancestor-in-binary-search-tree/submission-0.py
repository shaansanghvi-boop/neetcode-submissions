class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo = p if p.val < q.val else q
        hi = q if p.val < q.val else p
        
        def dfs(cur):
            if not cur:
                return None
            if lo.val <= cur.val <= hi.val:
                return cur
            elif cur.val < lo.val:
                return dfs(cur.right)
            else:
                return dfs(cur.left)
                
        return dfs(root)