class Solution:
    def get_next_unvisited(self, N: int, visited: dict, times: List[int]) -> int:
        # (node, node_distance)
        min_node_dist = (-1, 101)
        
        for i in range(N):
            if not visited[i] and min_node_dist[1] > times[i]:
                min_node_dist = (i, times[i])
        
        return min_node_dist[0]
        
        
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # build time_dict
        time_dict = {i:[101 for _ in range(N)] for i in range(N)}
        for i in range(N):
            time_dict.get(i)[i] = 0

        # fill time_dict
        for source, target, time in times:
            time_dict[source - 1][target - 1] = time
        
        # times to other nodes from source
        times = time_dict.get(K - 1)
        visited = {i:False for i in range(N)}
        visited[K - 1] = True
        node = self.get_next_unvisited(N, visited, times)
        
        while node != -1:
            visited[node] = True
            time_to_parent = times[node]
            
            for i in range(N):                
                if not visited[i]:
                    time_to_node = time_dict.get(node)[i]

                    if times[i] > time_to_node + time_to_parent:
                        times[i] = time_to_node + time_to_parent
                        
            node = self.get_next_unvisited(N, visited, times)

        max_time = 0
        
        for time in times:
            if time == 101:
                return -1
            elif time > max_time:
                max_time = time
                
        return max_time
                    
        
