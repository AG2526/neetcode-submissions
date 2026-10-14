class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0                      # NEW: how many nodes visited so far

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1                 # NEW: visiting this node
            if n == k:             # NEW: is this the kth smallest?
                return cur.val
            cur = cur.right