class Solution:
    surroundings = [(0,-1), (0, 1), (-1, 0), (1, 0)]

    def explore_surroundings(self, visited: List[int], grid: List[List[int]], row: int, col: int) -> int:
        perimeter = 0
        cell = grid[row][col]
        
        for x, y in self.surroundings:
            row_pos = x + row
            col_pos = y + col
            
            if 0 <= row_pos < len(grid) and 0 <= col_pos < len(grid[row]):
                if visited[row_pos][col_pos] == -1 and grid[row_pos][col_pos] == 1:
                    perimeter += 1 if cell == 0 else 0  # within the matrix, unvisited, and is land

                elif visited[row_pos][col_pos] == -1 and grid[row_pos][col_pos] == 0:
                    perimeter += 1 if cell == 1 else 0  # within the matrix, unvisited, and is water
           
            elif cell == 1:
                perimeter += 1  # off the grid and is water

        return perimeter
                
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        perimeter = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                visited[row][col] = 0  # mark as visited
                perimeter += self.explore_surroundings(visited, grid, row, col)

        return perimeter
