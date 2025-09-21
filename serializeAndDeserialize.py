# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # initialize the new string as an array
        res = []

        # dfs (node):
        def dfs(node):
            # base case:
            # if the node is None:
            if not node:
                # add it to the string
                res.append("N")
                return None

            # recurse
            # add the node to the string
            res.append(str(node.val))
            # recurse on the left subtree
            dfs(node.left)
            # recurse on the right subtree
            dfs(node.right)

        # run the dfs on the root node
        dfs(root)
        # return the new_str
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
