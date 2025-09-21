from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
                top = stack[-1]
                # if the top element's height is the same as the curr element's height:
                if top[1] == heights[i]:
                    # they should have the same topIdx
                    topIdx = top[0]
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


print(Solution().largestRectangleArea([2, 2, 5, 6, 2, 3]))
