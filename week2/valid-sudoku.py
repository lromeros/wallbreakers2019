class Solution:
    def get_square(self, x, y, board):
        square = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                square.append(board[x+i][y+j])
        return square
    def validate_group(self, group):
        group = [i for i in group if i != '.']
        unique_vals = set(group)
        
        return len(group) == len(unique_vals)
        
    def validateCols(self, board):
        for col in board:
            if not self.validate_group(col):
                return False
        return True
    
    def validateSquares(self, board):
        coords = []
        for i in [1,4,7]:
            for j in [1,4,7]:
                coords.append((i, j))
        squares = [self.get_square(x, y, board) for x, y in coords]
        
        for s in squares:
            if not self.validate_group(s):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rotated = copy.deepcopy(board)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                rotated[j][i] = board[i][j]
                
        if self.validateCols(board):
            if self.validateCols(rotated):
                if self.validateSquares(board):
                    return True
                
        return False
