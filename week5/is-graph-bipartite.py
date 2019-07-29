class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0 for _ in range(len(graph))]
        
        for i in range(len(graph)):
            if colors[i] == 0:
                colors[i] = 1
                queue = [i]
                
                while len(queue) > 0:
                    node = queue.pop()

                    for edge in graph[node]:
                        if colors[node] == colors[edge]:
                            return False
                        elif colors[edge] == 0:
                            colors[edge] = colors[node] * -1
                            queue.append(edge)
        
        return True
