# 2236. Root Equals Sum of Children
# https://leetcode.com/problems/root-equals-sum-of-children/description/
# Beats: 100.00% [Copied from solutions]
def checkTree(self, root: Optional[TreeNode]) -> bool:
    return root.val == root.left.val + root.right.val
