from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS (Optimal)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [0]

        def dfs(node):
            if not node:
                return None

            if low <= node.val <= high:
                ans[0] += node.val
            if low < node.val:
                dfs(node.left)
            if high > node.val:
                dfs(node.right)

        dfs(root)

        return ans[0]

    # BFS
    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        total = 0

        while queue:
            node = queue.pop()
            if low <= node.val <= high:
                total += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return total
