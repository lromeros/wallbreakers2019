class Solution:
    
    def get_valid_neighbors(self, row: int, col: int, matrix: List[List[int]], positions_used):
        surrounding = [(0,-1), (1,0), (0,1), (-1, 0)]
        valid_neighbors = []

        for x, y in surrounding:
            row_delta = row + x
            col_delta = col + y
            
            if 0 <= row_delta < len(matrix) and 0 <= col_delta < len(matrix[row]) and (row_delta, col_delta) not in positions_used:
                valid_neighbors.append((row_delta, col_delta))
        
        return valid_neighbors
    
    
    def dfs_longest(self, last_val: int, row: int, col: int, matrix: List[List[int]], max_paths: List[List[int]], positions_used) -> int:
        cell = matrix[row][col]
        max_path = 0

        if last_val < cell:
            max_path += 1

            if max_paths[row][col] != 0:
                return max_paths[row][col]
            
            positions_used.append((row, col))
            
            for n_row, n_col in self.get_valid_neighbors(row, col, matrix, positions_used):
                n_path = 1 + self.dfs_longest(cell, n_row, n_col, matrix, max_paths, positions_used)
                
                if n_path > max_path:
                    max_path = n_path
                    
            positions_used.remove((row, col))
            max_paths[row][col] = max_path
        
        return max_path
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_paths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        if len(matrix) < 1:
            return 0
        
        max_length = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                path_length = self.dfs_longest(-1, row, col, matrix, max_paths, [])

                if path_length > max_length:
                    max_length = path_length
                
        return max_length
