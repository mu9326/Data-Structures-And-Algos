def BFSGraph(graph, source, needle):
    # initialize the queue
    # add the source to the queue

    # initialize the path

    # initialize a visited set

    # visited = {0, 1}
    # queue = [3]
    # path = [0, 2]
    # while the queue is not empty:
    # pop the first node off the queue
    # if we have seen this node:
    # continue
    # add it to the path
    # check if this is our needle:
    # if it is:
    # return the path

    # add the neighbours to the queue
    # pop the node from the path
    pass


graph = [
    [0, 1, 4, 5, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0],
]
print(BFSGraph(graph, 0, 4))
