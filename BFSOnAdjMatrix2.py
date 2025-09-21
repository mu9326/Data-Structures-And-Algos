from collections import deque


class GraphEdge:
    __slots__ = "to", "weight"

    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

    def __repr__(self):
        return f"{{to: {self.to}, weight: {self.weight}}}"


def BFSGraph(graph, source, needle):
    # initialize seen and prev
    seen = [False for _ in range(len(graph))]
    prev = [-1 for _ in range(len(graph))]
    print(seen, prev)
    # seen[source] = T
    seen[source] = True
    queue = deque()
    queue.append(source)

    # while the queue is not empty:
    while queue:
        curr = queue.popleft()

        # if curr is the needle:
        if curr == needle:
            break

        # explore the neighbours of curr:
        neighbours = graph[curr]
        for nei in neighbours:
            print("nei: ", nei, " of ", curr)
            # if the neighbour is in seen:
            if seen[nei.to]:
                continue

            seen[nei.to] = True
            prev[nei.to] = curr
            print("prev: ", prev)
            queue.append(nei.to)

    # if the needle is found (i.e. prev[needle] != -1)
    if prev[needle] != -1:
        path = [needle]
        # use a while loop to get to -1 (source)
        curr = prev[needle]
        while curr != -1:
            # add the curr to the path
            path.append(curr)
            # update the curr
            curr = prev[curr]

    # add the source to the path
    return path[::-1]


# graph = [
#     [0, 1, 4, 5, 0],
#     [1, 0, 0, 0, 0],
#     [0, 0, 0, 2, 0],
#     [0, 0, 0, 0, 5],
#     [0, 0, 0, 0, 0],
# ]

graph = [
    [GraphEdge(1, 1), GraphEdge(3, 5), GraphEdge(2, 4)],
    [GraphEdge(0, 1)],
    [GraphEdge(3, 2)],
    [GraphEdge(4, 5)],
    [],
]
print("[")
for edges in graph:
    print(f" {edges},")
print("]")
print(BFSGraph(graph, 0, 4))
