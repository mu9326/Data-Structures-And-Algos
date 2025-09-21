class MinHeap:
    __slots__ = ("data", "length")

    def __init__(self):
        self.data = []
        self.length = 0

    def insert(self, value):
        self.data.append(value)
        self.heapifyUp(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            return None

        deletedV = self.data[0]

        if self.length == 1:
            self.data = []
            self.length -= 1
            return deletedV

        # swap the elements at the first index and the last index
        self.data[0] = self.data[self.length - 1]
        self.length -= 1

        # heaoifydown with the first index
        self.heapifyDown(0)

        return deletedV

    def __str__(self):
        return str(self.data[: self.length])

    def heapifyUp(self, index: int) -> None:
        # base case:
        if index == 0:
            return

        # Get the parent of the index
        parentIdx = self.parent(index)
        # Get the value of the parent at the index
        parentV = self.data[parentIdx]
        # Get the value of the index
        currV = self.data[index]

        # check if value of parent is greater than value at the index
        if parentV > currV:
            # if it is, swap the two values
            self.swap(index, parentIdx)

            # heapifyUp with the parent index
            self.heapifyUp(parentIdx)

    def heapifyDown(self, index):
        # base case - if index is out of range of the array
        if index >= self.length:
            return

        leftIdx, rightIdx = index, index

        # recursive case
        # check if left child exists - get the left child of the index
        # check if right child exists - get the right child of the index
        if self.left_child(index) < self.length:
            leftIdx = self.left_child(index)

        leftV = self.data[leftIdx]

        if self.right_child(index) < self.length:
            rightIdx = self.right_child(index)

        rightV = self.data[rightIdx]

        currV = self.data[index]

        # swap the index with the value at the minimum of two children
        if leftV < rightV and leftV < currV:
            self.swap(index, leftIdx)
            self.heapifyDown(leftIdx)
        elif rightV < leftV and rightV < currV:
            self.swap(index, rightIdx)
            self.heapifyDown(rightIdx)

    def swap(self, index1, index2):
        parentV = self.data[index2]
        # Get the value of the index
        currV = self.data[index1]
        self.data[index1] = parentV
        self.data[index2] = currV

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2
