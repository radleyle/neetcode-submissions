class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # declare a hash map where the key is cols and the values is a hash set
        rows = collections.defaultdict(set) # same as above
        squares = collections.defaultdict(set) # same as above but key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]): #rows[r] represents a hash set of all values that occur in row r, if board[r][c] (current number we're at) is already in rows[r] or cols[c] or in the current square before, that means it's a duplicate
                    return False
                cols[c].add(board[r][c]) # if its valid, update all 3 hash maps up above by adding to it the character we just saw
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True