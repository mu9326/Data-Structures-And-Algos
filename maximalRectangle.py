from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            # initialize the stack
            stack = []
            maxArea = 0

            # iterate over heights
            for i in range(len(heights)):
                topIdx = i
                # if the stack is not empty:
                if len(stack) != 0:
                    # while the height of the top element on the stack is greater than the current height
                    while len(stack) != 0 and stack[-1][1] > heights[i]:
                        top = stack[-1]
                        area = (i - top[0]) * top[1]
                        # update maxArea as per the index (currIdx - element's index) and height of the top element
                        maxArea = max(area, maxArea)

                        # store the topIdx in a variable - we need it later to append the current element
                        topIdx = top[0]
                        # pop the top element
                        stack.pop()
                    # if the top element's height is the same as the curr element's height:
                    if len(stack) != 0 and stack[-1][1] == heights[i]:
                        # they should have the same topIdx
                        topIdx = stack[-1][0]
                    # add the curr element with top element's index
                    stack.append([topIdx, heights[i]])
                else:
                    # append the [index, height]
                    stack.append([i, heights[i]])

            # while the stack is not empty:
            while len(stack) != 0:
                top = stack[-1]
                area = (len(heights) - top[0]) * top[1]
                # calculate the max area
                maxArea = max(area, maxArea)
                # pop the indices one by one
                stack.pop()

            return maxArea

        n = len(matrix)
        m = len(matrix[0])

        prefix_sums = [[0 for _ in range(m)] for _ in range(n)]

        # calculate the prefix sums matrix
        for c in range(m):
            prefix_sum = 0
            for r in range(n):
                if matrix[r][c] == "1":
                    prefix_sum += 1
                    prefix_sums[r][c] = prefix_sum
                else:
                    prefix_sum = 0

        maxArea = 0
        for r in range(n):
            area = largestRectangleArea(prefix_sums[r])
            maxArea = max(area, maxArea)

        return maxArea
