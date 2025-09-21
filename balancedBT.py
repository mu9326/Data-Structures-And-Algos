# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not root:
                return None

            # recursive case
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            return 1 + max(left_height, right_height)

        if abs(dfs(root.left) - dfs(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        # DFS

        pass
