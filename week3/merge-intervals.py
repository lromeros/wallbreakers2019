class Solution:
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        merged = []
        last_elem = intervals[0]
        
        for i in range(1, len(intervals)):
            start, end = last_elem
            next_start, next_end = intervals[i]
            
            if next_start >= start and next_start <= end:
                merged_end = end if end > next_end else next_end
                last_elem = [start, merged_end]
            else:
                merged.append(last_elem)
                last_elem = intervals[i]
        
        merged.append(last_elem)
        return merged
