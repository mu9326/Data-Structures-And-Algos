from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        if rows == 1 and cols == 1 and word == board[0][0]:
            return True

        # dfs funtion(r, c, index)
        def dfs(r, c, index):
            # if index is out of range:
            if index == len(word):
                return True

            # if the value at r,c is not equal to the letter at the index or cell == '#':
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            # mark the cell as '#'
            board[r][c] = "#"
            # else: explore the neighbours of this cell
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                # for each neighbour --> call dfs on the nei coords and the next index
                if dfs(r + dr, c + dc, index + 1):
                    return True

            return False

        # for each letter in board, run dfs on each grid position (starting with index 1 of the letter)
        for r in range(rows):
            for c in range(cols):
                # if any dfs call results in True:
                if dfs(r, c, 0):
                    return True

        return False


# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"

board = ["A"]
word = "A"

print(Solution().exist(board, word))
