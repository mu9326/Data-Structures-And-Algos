# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # initialize a count variable
        count = [0]

        # write a dfs function that takes the node as the parameter
        def dfs(node):
            # base case:
            # if the node is None:
            if not node:
                return (0, 0)

            # get the left sum and number of nodes in the left subtree
            totalL, numL = dfs(node.left)
            # get the right sum and number of nodes in the right subtree
            totalR, numR = dfs(node.right)

            # add the node's current value to the sum and divide it by num_left + num_right + 1
            total = totalL + totalR + node.val
            num = numL + numR + 1
            average = total // num
            # if the value is equal to the average:
            if node.val == average:
                # increase the count
                count[0] += 1

            # return the sum and the num of nodes
            return (total, num)

        # call the dfs function with node as the parameter
        dfs(root)

        # return count
        return count[0]
