from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not inorder:
            return None

        # recursive case
        # preorder = [9, 11]
        # inorder = [11, 9]

        # create a new node with root as its value
        node = TreeNode(preorder[0])  # root = 9
        mid = inorder.index(preorder[0])  # mid = 1
        print("mid: ", mid)

        # construct the left subtree
        # preorder = [11]
        # inorder = [11]
        node.left = self.buildTree(preorder[1 : mid + 1], inorder[0:mid])

        # construct the right subtree
        # preorder = []
        # inorder = []
        node.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return node

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    # HASHMAP + DFS
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hashmap to store the indices of values in preorder
        indices = {val: idx for idx, val in enumerate(inorder)}

        # initialize a pointer
        self.pre_idx = 0

        # recursive function
        def dfs(l, r):
            # base case is if the left pointer surpasses the right
            if l > r:
                return None

            # get the index of the root value
            root_val = preorder[self.pre_idx]
            # increase the pointer
            self.pre_idx += 1

            # make a node and get the index of the root value from the indices list
            root = TreeNode(root_val)
            mid = indices[root_val]

            # instead of slicing, use the left and right pointers to divide the inorder list
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        # call the recursive function - left pointer is 0 and right pointer is at the last val of the list (preorder and inorder are of the same length)
        return dfs(0, len(inorder) - 1)

    def buildTree3(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0

        # recursive function
        def dfs(limit):
            # global variables
            nonlocal preIdx, inIdx

            # base cases
            # preIdx = 2
            # inIdx = 0
            # limit = inf
            if preIdx >= len(preorder):
                return None
            # if the value of inIdx in the inorder array is equal to the limit, increase the inIdx by 1
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            # root = 20
            root = TreeNode(preorder[preIdx])
            # preIdx = 3
            preIdx += 1

            # left limit - 20
            # right limit - inf
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float("inf"))
