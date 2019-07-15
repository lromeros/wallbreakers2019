class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        
        points.sort()
        balloon_dims = [] 
        last_balloon = points[0] if len(points) > 0 else []
        
        for i in range(1, len(points)):
            start, end = last_balloon
            next_start, next_end = points[i]
            if next_start <= end:
                merged_start = max(start, next_start)
                merged_end = min(end, next_end)
                last_balloon = [merged_start, merged_end]
            else:
                balloon_dims.append(last_balloon)
                last_balloon = points[i]

        balloon_dims.append(last_balloon)            
        return len(balloon_dims)
