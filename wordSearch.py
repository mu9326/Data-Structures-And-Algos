from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(idx, row, col, visited):
            # backtrack function(idx, row-coord, col-coord, visited set): # 2, 0, 0, [A, C, E]
            # if the idx is out of range:
            # return true

            # if char at idx matches the char in the grid # true
            print("Checking for idx = ", idx, " i.e., ", word[idx])
            if word[idx] == board[row][col]:
                if idx == len(word) - 1:
                    print("Returning true")
                    return True
                # add the element to visited
                visited.add((row, col))
                print("Visited: ", visited)
                # increase idx by 1 and explore all four directions for cells that
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (
                        0 <= (row + dr) < rows
                        and 0 <= (col + dc) < cols
                        and (row + dr, col + dc) not in visited
                    ):
                        # are not in visited and that are within bounds
                        if backtrack(idx + 1, row + dr, col + dc, visited):
                            return True

                visited.remove((row, col))

            # return false
            return False

        rows, cols = len(board), len(board[0])
        # iterate over the grid and run the backtrack solution on each cell -
        for r in range(rows):
            for c in range(cols):
                visited = set()
                # if any of them comes back as true
                if backtrack(0, r, c, visited):
                    print("Final true")
                    return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
print(Solution().exist(board, word))
