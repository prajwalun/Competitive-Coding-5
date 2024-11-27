# The isValidSudoku method checks whether a given Sudoku board is valid.

# Step 1: Use a Set for Validation
#   - The set 'res' tracks seen elements in rows, columns, and sub-boxes.
#   - Each entry is represented as a tuple:
#       - (row index, element) for rows.
#       - (element, column index) for columns.
#       - (sub-box index, element) for sub-boxes.

# Step 2: Iterate Through the Board
#   - For each non-empty cell:
#       - Check if the element already exists in its row, column, or sub-box in 'res'.
#       - If it does, the board is invalid, return False.
#       - Otherwise, add the corresponding tuples to 'res'.

# Step 3: Return Result
#   - If no duplicates are found, return True, indicating the board is valid.

# TC: O(1) - Fixed size 9x9 board makes the checks constant time.
# SC: O(1) - Space for the set is proportional to the board size, which is constant.


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a set to store tuples representing rows, columns, and sub-boxes
        res = set()

        for i in range(9):
            for j in range(9):
                element = board[i][j]

                if element != '.':
                    if((i, element) in res or (element, j) in res or (i //3, j//3, element) in res):
                        return False
                res.add((i, element))
                res.add((element, j))
                res.add((i//3,j//3,element))
        return True