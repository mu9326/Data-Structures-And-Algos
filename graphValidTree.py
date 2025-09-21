from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        graph = [[] for _ in range(n)]
        # construct the graph
        for edge in edges:  # [0, 1]
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # initialize the visited set and the prev array
        visited = set()
        prev = [-1 for _ in range(n)]

        # begin DFS
        def dfs(node):
            # if the node is in visited (i.e. cycle present):
            if node in visited:
                return False

            # mark the node as visited
            visited.add(node)
            # explore its neighbours
            neighbours = graph[node]
            for nei in neighbours:
                # if the prev[node] is not equal to the nei:
                if prev[node] != nei:
                    # mark prev of nei as node
                    prev[nei] = node
                    if not dfs(nei):
                        return False

            return True

        # if dfs(0) is True:
        if dfs(0) and len(visited) == n:
            return True

        return False


print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4], [4, 2]]))
print(Solution().validTree(4, [[0, 1], [1, 2], [2, 0], [2, 3]]))
