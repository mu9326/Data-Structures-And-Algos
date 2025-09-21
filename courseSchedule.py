from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize a visted and a visiting array - filled with 0's
        # visting = [1, 1, 1, 1, 1], visited = [1, 1, 1, 1, 1]
        visiting = [False for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]

        # construct the graph
        # adjlist --> [[] for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        print("graph :", graph)

        # for each element in prereq - [[1, 0]]
        for c in prerequisites:  # [1, 0]
            # elemnt at position 0 --> [element at position 1] # append this
            graph[c[0]].append(c[1])

        # graph = [[1], [], [3, 1], [4], []]
        print("graph :", graph)

        # dfs(node coords) -> true/false
        def dfs(node):
            # base case:
            # if we have visited this node:
            if visited[node]:
                # return T
                return True

            # if we are visiting this node:
            if visiting[node]:
                # return F
                return False

            visiting[node] = True

            # if the node has no neighbours:
            if len(graph[node]) == 0:
                # mark node as visited and visiting
                visited[node] = True
                # return T
                return True

            # recurse step:
            # call the dfs function on every neighbour of the curr node -> if T, # 1
            neighbours = graph[node]
            print(neighbours)
            for nei in neighbours:
                if not dfs(nei):
                    # mark this curr node as visited
                    visited[node] = True
                    return False

            # mark this curr node as visited
            visited[node] = True
            return True

        for i in range(len(graph)):
            if not dfs(i):
                return False

        return True


numCourses = 3
prerequisites = [[1, 0], [1, 2], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
