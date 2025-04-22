from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS recrusive
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p and q:
            return False

        if not q and p:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # DFS iterative
    def isSameTreeIterDFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        stack = [(p, q)]

        while stack:
            node = stack.pop()
            p = node[0]
            q = node[1]

            # we are checking if both p and q are not None and that they
            # have the same values
            if p and q:
                if p.val != q.val:
                    return False
                else:
                    stack.append((p.left, q.left))
                    stack.append((p.right, q.right))
                    print("stack appended")

            # if we have reached this point, that means that:
            # either one of p or q or both is None
            # if either is none, we want to return False
            # if both are none, we don't do anything - we don't append them to the stack and we don't return False
            if (not p and q) or (not q and p):
                return False

        return True
