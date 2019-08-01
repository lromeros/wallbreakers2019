class Solution:
    
    def num_in_row(self, num: str, row: int, board: List[List[str]]) -> bool:
        for cell in board[row]:
            if cell == num:
                return True
        return False
    
    
    def num_in_col(self, num: str, col: int, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if board[i][col] == num:
                return True
        return False
    
    
    def _get_cell_square_id(self, row: int, col: int) -> int:
        row_id = math.floor(row / 3)
        col_id = math.floor(col/3)
        
        return (row_id * 3) + col_id
    
    
    def _get_square_ranges(self, row: int, col: int) -> List[int]:
        square_id_ranges = {0:[3,3],
                           1:[3,6],
                           2:[3,9],
                           3:[6,3],
                           4:[6,6],
                           5:[6,9],
                           6:[9,3],
                           7:[9,6],
                           8:[9,9]}
        
        square_id = self._get_cell_square_id(row, col)
        return square_id_ranges.get(square_id)
    
    
    def num_in_square(self, num: str, row: int, col: int, board: List[List[str]]) -> bool:
        row_max, col_max = self._get_square_ranges(row, col)
        
        for row in range(row_max - 3, row_max):
            for col in range(col_max - 3, col_max):
                if board[row][col] == num:
                        return True
        return False
            
        
    def valid_placement(self, num: str, row: int, col: int, board: List[List[str]]) -> bool:
        return not self.num_in_square(num, row, col, board) and not self.num_in_col(num, col, board) and not self.num_in_row(num, row, board)
    
    
    def sudoku_recur(self, row: int, col: int, board: List[List[str]]) -> bool: 
        if col == len(board[0]):
            col = 0
            row += 1
            
            if row == len(board):
                return True
        
        if board[row][col] == '.':
            for i in range(1, 10):
                if self.valid_placement(str(i), row, col, board):
                    board[row][col] = str(i)
                    if self.sudoku_recur(row, col + 1, board):
                        return True
            board[row][col] = '.'
            return False
        else:
            return self.sudoku_recur(row, col + 1, board)
        
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        self.sudoku_recur(0, 0, board)

