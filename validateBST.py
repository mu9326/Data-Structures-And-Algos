from math import inf
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root, minimum, maximum):
        if (minimum < root.val < maximum) and not root.left and not root.right:
            return True

        leftFlag = False
        rightFlag = False

        if minimum < root.val < maximum:
            if root.left:
                leftFlag = self.helper(root.left.val, minimum, root.val)
            else:
                leftFlag = True

            if root.right:
                rightFlag = self.helper(root.right.val, root.val, maximum)
            else:
                rightFlag = True

        return leftFlag and rightFlag

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.val, -inf, inf)
