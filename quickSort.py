from typing import List


def quickSort(array: List[int]) -> List[int]:
    def qs(array, low, high):
        # base case:
        if high - low == 0 or high - low == 1:
            return array

        i = low - 1

        pivot = array[high]

        # traverse over the array with the j pointer
        for j in range(low, high):  # O(n)
            # compare the value at j and pivot
            if array[j] <= pivot:
                i += 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

        # recurse on the left half of the array (array[0:i])
        left = qs(array, 0, i - 1)

        # recurse on the right half of the array (array[i+1:])
        right = qs(array, i + 1, len(array) - 1)

        return array

    qs(array, 0, len(array) - 1)


print(quickSort([8, 2, 4, 7, 1, 3, 9, 6, 5]))
print(quickSort([4, 1]))
