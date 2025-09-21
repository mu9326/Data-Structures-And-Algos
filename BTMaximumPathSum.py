from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = [root.val]

        def dfs(node):
            if node is None:
                return 0

            # calculate the max path sum of the left subtree
            left_sum = max(dfs(node.left), 0)

            # calculate the max path sum of the right subtree
            right_sum = max(dfs(node.right), 0)

            # update res
            self.res[0] = max(node.val + left_sum + right_sum, self.res[0])
            # return the max(maxPath sum)
            path_sum = path_sum_left = path_sum_right = node.val
            if left_sum > 0:
                path_sum_left = node.val + left_sum
            if right_sum > 0:
                path_sum_right = node.val + right_sum
            return max(path_sum, path_sum_left, path_sum_right)

        dfs(root)

        return self.res[0]
