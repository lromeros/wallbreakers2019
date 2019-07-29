class Solution:
    word = ''
    positions_used = []
    
    def get_valid_children(self, row: int, col: int, board: List[List[str]]):
        surrounding = [(0,-1), (1,0), (0,1), (-1, 0)]
        valid_children = []

        for x, y in surrounding:
            row_delta = row + x
            col_delta = col + y
            
            if 0 <= row_delta < len(board) and 0 <= col_delta < len(board[row]) and (row_delta, col_delta) not in self.positions_used:
                valid_children.append((row_delta, col_delta))
        
        return valid_children
    
    
    def dfs(self, row: int, col: int, board: List[List[str]], word_i: int) -> bool:
        cell = board[row][col]

        if word_i == len(self.word) - 1 and self.word[word_i] == cell:
            return True
        elif self.word[word_i] == cell:
            self.positions_used.append((row, col))
            
            for child_row, child_col in self.get_valid_children(row, col, board):

                if self.dfs(child_row, child_col, board, word_i + 1):
                    return True
                
            self.positions_used.remove((row, col))
        else:
            return False
                        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        
        if len(self.word) == 0:
            return False
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if self.dfs(row, col, board, 0):
                    return True
