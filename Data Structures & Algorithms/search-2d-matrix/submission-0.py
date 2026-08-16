class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) # get the dimensions of the matrix

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2 # implement binary search
            if target > matrix[row][-1]: # look at the right most value of that row
                top = row + 1 # look at the larger row if the target is bigger
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        # do binary search on the target row determined
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False