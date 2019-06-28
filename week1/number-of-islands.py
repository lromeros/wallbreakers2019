class Solution:
    class IslandGroups:
        def __init__(self, width, height):
            self.height = height
            self.ids = [i for i in range(width * height)]
            self.island_count = width * height
            
        def get_iid(self, i, j):
            return i * self.height + j
        
        def is_new_island(self, i, j):
            return self.find_parent_island(i, j) == self.get_iid(i, j)
        
        def find_parent_island(self, i, j):
            iid = self.get_iid(i, j)
            parent = iid
            
            while parent != self.ids[parent]:
                parent = self.ids[parent]
                
            self.path_compress(iid, parent)
            return parent
        
        def path_compress(self, iid, pid):
            while iid != pid:
                member = copy.deepcopy(self.ids[iid])
                self.ids[iid] = pid
                iid = member
                
        def union_islands(self, i1, j1, i2, j2):
            parent1 = self.find_parent_island(i1, j1)
            parent2 = self.find_parent_island(i2, j2)
            
            if parent1 != parent2:
                self.ids[parent2] = parent1
                self.island_count -= 1
            
            
            
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        islands = self.IslandGroups(len(grid), len(grid[0]))
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if j + 1 < len(grid[0]):
                        if grid[i][j+1] == '1':
                            islands.union_islands(i, j, i, j+1)
                    if i + 1 < len(grid):
                        if grid[i+1][j] == '1':
                            islands.union_islands(i, j, i+1, j)
                else:
                    islands.island_count -= 1
                    # print("water[{}][{}], island_count = {}".format(i, j, islands.island_count))

        # print(islands.ids)
        return islands.island_count
