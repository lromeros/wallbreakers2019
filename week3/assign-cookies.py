class Solution:
    def findContentChildren(self, greed: List[int], sizes: List[int]) -> int:
        happy_children = 0
        greed.sort()
        sizes.sort()
        i = 0
        
        for j in range(len(sizes)):
            if i < len(greed) and sizes[j] >= greed[i]:
                happy_children += 1
                i += 1
            
        
        return happy_children
