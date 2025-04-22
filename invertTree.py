# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTreeDFS(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def invertTreeBFS(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None  # If the tree is empty, return None

        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            current = queue.popleft()  # Dequeue the next node

            # Swap the left and right children
            current.left, current.right = current.right, current.left

            # Enqueue the children to process them in the next levels
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root  # Return the root of the inverted tree
