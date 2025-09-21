from collections import deque


def BFSGraph(graph, source, needle):
    # initialize the seen and previous arrays
    seen = [False] * len(graph)
    print(seen)
    prev = [-1] * len(graph)

    # add source to the queue
    queue = deque()
    # turn the seen of source to True
    queue.append(source)
    seen[source] = True
    # set curr = source = queue.pop()

    while queue:
        # do-while loop (while queue.length) -
        curr = queue.pop()

        if curr == needle:
            break

        # iterate over the elements in the curr
        connections = graph[curr]
        print("Connections of ", curr, ": ", connections)

        for c in range(len(connections)):
            print("c: ", c)
            if connections[c] != 0:
                print("c that is not 0: ", c)
                if seen[c]:
                    continue
                queue.append(c)
                prev[c] = curr
                seen[c] = True

    # if we have already seen the element:
    # continue
    # add the connected nodes of the curr to the queue
    # turn the prev of the element to source
    # turn seen for the curr to True

    if prev[needle] == -1:
        return []
    # if path not found - return None
    # else - build the path backwards and return it
    curr = needle
    print("curr: ", curr)
    print("prev: ", prev)
    path = []

    while prev[curr] != -1:
        path.append(curr)
        curr = prev[curr]

    path.reverse()
    print("path: ", path)
    res = [source] + path
    return res


graph = [
    [0, 1, 4, 5, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0],
]
print(BFSGraph(graph, 0, 4))
