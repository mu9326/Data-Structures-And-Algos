from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        border = []
        m, n = len(board), len(board[0])
        # iterate over the grid and add the border 0 cells to the border array
        for i in range(0, n):
            if board[0][i] == "O":
                border.append((0, i))

        for j in range(0, n):
            if board[m - 1][j] == "O":
                border.append((m - 1, j))

        for i in range(1, m - 1):
            if board[i][0] == "O":
                border.append((i, 0))

        for j in range(1, m - 1):
            if board[j][n - 1] == "O":
                border.append((j, n - 1))

        # print("border", border)

        # dfs (coords):
        def dfs(r, c):
            if board[r][c] == "#" or board[r][c] == "X":
                return

            # recursive case
            # change the value of the cell to '#'
            board[r][c] = "#"
            # iterate over its neighbors:
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                # if the neighbor is not equal to "#" or "X" or the neighbor is within range:
                if (
                    0 <= r + dr < m
                    and 0 <= c + dc < n
                    and board[r + dr][c + dc] != "X"
                    and board[r + dr][c + dc] != "#"
                ):
                    # call the dfs on the neighbor
                    dfs(r + dr, c + dc)

        # print(board)

        # iterate over the border array:
        for cell in border:
            r, c = cell
            # call dfs on every element of the border array
            dfs(r, c)

        # print(board)

        # iterate over our modified grid and find all '0's and change them to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"

        # print(board)


# board = [
#     ["X", "X", "X", "X"],
#     ["X", "O", "O", "X"],
#     ["X", "X", "O", "X"],
#     ["X", "O", "X", "X"],
# ]

board = [
    ["O", "X", "X", "O"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "X", "X", "O"],
    ["X", "O", "O", "X"],
    ["X", "O", "X", "X"],
]

# sol = [(0, 0), (0, 3), (3, 3), (5, 1)]
print(Solution().solve(board))
