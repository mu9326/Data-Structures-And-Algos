from typing import List


def DFSGraph(graph, source, needle) -> List[int]:
    def walk(graph, source, needle, path, seen):
        # base case:
        # if we have found the needle
        if source == needle:
            # add the source to the path and return it
            return [source]

        # if we have already seen the source:
        if seen[source]:
            # return path
            return []

        # recursive case
        # turn the seen of source to true
        seen[source] = True
        # iterate over the neighbours of source
        neighbours = graph[source]
        # path = recurse on each neighbor
        for nei in neighbours:
            result_path = walk(graph, nei[0], needle, path, seen)
            # if path is non-empty:
            if len(result_path) != 0:
                # add the source to the path
                # return path
                result_path.append(source)
                return result_path

        return []

    seen = [False for _ in range(len(graph))]
    # seen[source] = True

    path = walk(graph, source, needle, [], seen)

    return path[::-1]


graph = {0: [(1, 1), (2, 4)], 1: [(0, 1)], 2: [(3, 2)], 3: [(4, 5)], 4: []}
print(DFSGraph(graph, 0, 4))

graph = {
    0: [(1, 1), (2, 1)],
    1: [(3, 1)],
    2: [(4, 1)],
    3: [],  # dead-end (does not lead to 5)
    4: [(5, 1)],
    5: [],
}
print(DFSGraph(graph, 0, 5))
