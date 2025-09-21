from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # {0: [1, 2], 1: [4], 4: []}
        # build an adjacency list of the graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        print(graph)

        # initialize the res array
        order = []

        # initialize the states
        UNVISITED, VISITING, VISITED = 0, 1, 2

        # store the states in an array (each index will have one of 0, 1, 2 as its state)
        states = [UNVISITED for _ in range(numCourses)]

        # dfs(index):
        def dfs(index):
            # base case
            # if we have already visited this node (i.e. the state is 1):
            if states[index] == VISITING:
                return False

            # if the state is 2, return True
            if states[index] == VISITED:
                return True

            # mark as visiting
            states[index] = VISITING
            # explore its neighbours (i.e. outgoing edges):
            for i in graph[index]:
                if not dfs(i):
                    return False
            states[index] = VISITED
            order.append(index)

            return True

        # return res

        # begin dfs on index
        for i in range(numCourses):
            # if any index does not return dfs:
            if not dfs(i):
                return []

        return order


print(Solution().findOrder(5, [[0, 1], [1, 4], [0, 2], [2, 3], [3, 1], [3, 4]]))
