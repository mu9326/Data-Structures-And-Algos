from typing import Optional


# Given the root of a binary search tree and a target value, return the value in the BST that is
# closest to the target. If there are multiple answers, print the smallest.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # recursive function which takes the node as a parameter
        # base case:
        # if the node is None:
        # return closest
        pass
