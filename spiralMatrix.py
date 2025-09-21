from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        top, left = 0, 0
        bottom, right = rows, cols
        res = []

        while top < bottom or left < right:
            # print all the elements in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # print all the elements in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # print all the elements in the bottom row (but in reverse)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # print all the elements in the left col (but in reverse)

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))
