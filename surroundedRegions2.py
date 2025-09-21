from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # dfs function
        def dfs(r, c):
            # base case:
            # if the cell is not equal to 'O':
            if board[r][c] != "O":
                return

            # recursive case:
            board[r][c] = "#"
            # change the value to '#'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # iterate over the cells neighbors and recurse on each (condition: neighbor should be within bounds
                # equal to '0')
                if (
                    0 <= r + dr < rows
                    and 0 <= c + dc < cols
                    and board[r + dr][c + dc] == "O"
                ):
                    dfs(r + dr, c + dc)

        # iterate over the border cells -
        for r in range(rows):
            # if they are equal to 'O':
            if board[r][0] == "O":
                # run a DFS on their coords
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)

            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # iterate over the board - O(m * n)
        # 1. Change the remaining 'O's to #
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
