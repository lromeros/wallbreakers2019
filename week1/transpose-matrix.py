class Solution:
    def build_results_matrix(self, A):
        matrix = []
        
        for i in range(len(A[0])):
            row = [0] * len(A)
            matrix.append(row)
            
        return matrix
    
    
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        results = self.build_results_matrix(A)
        
        for i in range(len(A)):
            col = A[i]
            for j in range(len(col)):
                val = col[j]
                results[j][i] = val
                
        return results
