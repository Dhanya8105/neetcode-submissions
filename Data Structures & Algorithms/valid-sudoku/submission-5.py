class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set) #cuz list can have duplicates and set cannot have duplicates...
        cols=defaultdict(set)
        squares=defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                    #referrring to empty cell
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])#set uses add while lists append
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
        return True
