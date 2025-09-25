from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 1st pass
        parentMap = {root: root}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                parentMap[node.left] = node
                queue.append(node.left)
            if node.right:
                parentMap[node.right] = node
                queue.append(node.right)

        # # 2nd pass
        # stack = [root]
        # found = None
        # while stack:
        #     s = stack.pop()

        #     if s.right:
        #         stack.append(s.right)
        #     if s.left:
        #         stack.append(s.left)

        # 3rd pass
        visited = set()
        queue1 = deque([target])
        # visited.add(target)
        distance = 0

        while queue1:
            if distance == k:
                return [node.val for node in queue1]

            for _ in range(len(queue1)):
                node = queue1.popleft()
                visited.add(node)
                if node.left and node.left not in visited:
                    queue1.append(node.left)
                    # visited.add(node.left)
                if node.right and node.right not in visited:
                    queue1.append(node.right)
                    # visited.add(node.right)
                parent = parentMap[node]
                if parent not in visited:
                    queue1.append(parent)
                    # visited.add(parent)

            distance += 1

        return []
