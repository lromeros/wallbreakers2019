class Solution:
    def regexEquals(self, a: str, b: str) -> bool:
        if b == '.':
            return True
        else:
            return a == b
    
    
    def make_pattern_str_list(self, p: str) -> List[str]:
        p_list = []
        
        for c in p:
            if c == '*':
                p_list[len(p_list) - 1] += c
            else:
                p_list.append(c)
            
        return p_list        
        
    def get_matrix_val(self, matrix: List[List[str]], i: int, j: int) -> int:
        if i >= 0 and j >= 0:
            return matrix[i][j]
        else:
            return 0
        
        
    def isMatch(self, s: str, p: str) -> bool:
        p_list = self.make_pattern_str_list(p)
        matrix = [[0 for _ in range(len(p_list) + 1)] for _ in range(len(s) + 1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matches = 0 <= i - 1 < len(s) and 0 <= j - 1 < len(p_list) and self.regexEquals(s[i - 1], p_list[j - 1][0])
                
                if i == 0 and j == 0:
                    matrix[i][j] = 1
                elif 0 <= j - 1 < len(p_list) and len(p_list[j - 1]) > 1:
                    matrix[i][j] = self.get_matrix_val(matrix, i, j-1) or (self.get_matrix_val(matrix, i-1, j-1) and matches) or (self.get_matrix_val(matrix, i-1, j) and matches)
                elif matches:
                    matrix[i][j] = self.get_matrix_val(matrix, i-1, j-1) == 1
      
        return bool(matrix[len(s)][len(p_list)])
