class Solution:
    
    def build_intervals_dict(self, S: str):
        intervals = {}
        
        for i in range(len(S)):
            if intervals.get(S[i]) is None:
                intervals[S[i]] = [i, i+1]
            else:
                intervals[S[i]][1] = i +1
                
        return intervals
    
    
    def partitionLabels(self, S: str) -> List[int]:
        intervals = self.build_intervals_dict(S)
        group_sizes = []
        last_value = [-1, -1]
        
        for value in intervals.values():
            if last_value == [-1, -1]:
                last_value = value
            elif value[0] < last_value[1]:
                last_value[1] = max(last_value[1], value[1])
            else:
                group_sizes.append(last_value[1] - last_value[0])
                last_value = value
                
        group_sizes.append(last_value[1] - last_value[0])
        
        return group_sizes
            
        
                
