from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k  # 4
        for n in nums:  # n log k
            self.add(n)

    def add(self, val: int) -> int:  # 8
        if len(self.data) < self.k:
            self.data.append(val)  #
            self.heapifyUp(len(self.data) - 1)  # O(log k)
        else:
            minV = self.data[0]  # 8
            if val > minV:  # 8 > 7
                self.data.pop(0)  # 7
                self.data.insert(0, val)  # 8
                # print("Heap after inserting new element at 0: ", self.data)
                self.heapifyDown(0)  # O (log k)
                # print("Heap after heaifying down: ", self.data)

        return self.data[0]

    def heapifyUp(self, index):
        if index == 0:
            return

        # get the parent index and element
        parentIdx = (index - 1) // 2  # 2 -1 // 2 = 0
        parentV = self.data[parentIdx]  # 7
        # get the curr value at index
        currV = self.data[index]  # 7

        # if curr is lesser than parent, swap their values
        if currV < parentV:
            # heapifyUp again on the parent
            self.data[index] = parentV
            self.data[parentIdx] = currV
            self.heapifyUp(parentIdx)

    def heapifyDown(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Check if left child exists and is smaller
        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left

        # Check if right child exists and is smaller
        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right

        # If a child is smaller, swap and continue heapifying down
        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDown(smallest)

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


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
