from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        k = k

        def helper(self, root):
            if not root:
                return

            self.helper(root.left)
            if count != k:
                count += 1
            else:
                return root.val
            self.helper(root.right)

        self.helper(root)
