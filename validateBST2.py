from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper):
            if node is None:
                return True

            if (
                helper(node.left, lower, node.val)
                and helper(node.right, node.val, upper)
                and lower < node.val < upper
            ):
                # if recurse(node.left) and recurse(node.right) and the curr node val is within upper and lower:
                return True

            return False

        # call the helper function - root, inf, -inf
        return helper(root, float("-inf"), float("inf"))
