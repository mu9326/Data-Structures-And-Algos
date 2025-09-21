from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        # find the root parent of the node
        def find(node):
            # initially set the res equal to the node
            res = node

            # while res is not equal to the parent of itself bceause then we can stop searching once when we have gotten to a node that is a parent of itself
            # cuz that means that we have found the root of the parent and we cannot go any higher
            while res != par[res]:
                # path compression (optimization)-> before we go to the parent, we will set the parent of res to its grandparent
                par[res] = par[par[res]]

                # update the curr pointer to its parent
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
