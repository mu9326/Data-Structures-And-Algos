from typing import Dict, List


def DFSGraph(graph, source, needle) -> List[int]:
    def walk(
        graph: Dict[int, List[int]],
        needle: int,
        curr: int,
        seen: List[bool],
        path: List[int],
    ) -> bool:
        # base cases -
        # add the curr to the path
        # path = []
        path.append(curr)
        # if we found the needle, we return true
        if curr == needle:
            return True

        # if we have already seen the element, we return false
        if seen[curr]:
            return False

        # turn the seen of the curr to True
        # seen = [T, T, T, T, T]
        seen[curr] = True

        # recurse step
        # get the connections of the curr node
        # connections = [graph[4]]]
        connections = graph[curr]
        # c = (3, 2)
        for c in connections:
            if walk(graph, needle, c[0], seen, path):
                return True
        # call the recursive function with this new current node
        # if the above call returns true, return true

        # remove the node from the path (that means we have exhausted our list and we didn't find our needle)
        path.pop()

        # return false
        return False

    curr = source
    path = []
    seen = [False] * len(graph)

    walk(graph, needle, curr, seen, path)

    return path


graph = {0: [(1, 1), (3, 5), (2, 4)], 1: [(0, 1)], 2: [(3, 2)], 3: [(4, 5)], 4: []}
print(DFSGraph(graph, 0, 4))
