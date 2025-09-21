# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            # base cases:
            # if the root is a leaf node:
            if not node:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)
            # if the left tree and the right tree both return None

            if not left and not right:
                return None
            # elif the left tree returns a value and the right tree returns None:
            elif left and not right:
                # return the left tree value
                return left
            # elif the left tree returns None and the right tree returns a value:
            elif right and not left:
                # return the right tree value
                return right
            else:
                # return the node itself
                return node

        return dfs(root)
