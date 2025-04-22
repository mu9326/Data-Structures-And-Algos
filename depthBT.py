from collections import deque
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS solution
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        maxDepth = 1

        while queue:
            node, depth = queue.popleft()
            maxDepth = max(depth, maxDepth)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return maxDepth

    # DFS solution
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        # base case:
        if not root:
            return 0
        # recursive case:
        return 1 + max(self.maxDepthDFS(root.left), self.maxDepthDFS(root.right))
