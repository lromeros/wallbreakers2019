class Solution:    
    class FriendGroups:
        def __init__(self, friend_count):
            self.ids = [i for i in range(friend_count)]
            self.group_count = friend_count
            
        def find_parent(self, fid):
            parent = fid
            
            while parent != self.ids[parent]:
                parent = self.ids[parent]
            return parent
        
        def union_groups(self, f1, f2):
            parent1 = self.find_parent(f1)
            parent2 = self.find_parent(f2)
    
            if parent1 != parent2:
                self.ids[parent2] = parent1
                self.group_count -= 1   
            
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        friend_groups = self.FriendGroups(len(M))
        
        for i in range(len(M) - 1):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    friend_groups.union_groups(i, j)
        return friend_groups.group_count                    
        
