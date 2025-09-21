from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node):
            # base case -> if there is a node in the dict, return the node
            if node in oldToNew:
                return oldToNew[node]

            # recurse step -> create a copy and add that copy to the dictionary
            # iterate over the neighbors of the original node and add each neighbor to the neighbors of the
            # copy (but after dfs has been done)
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
