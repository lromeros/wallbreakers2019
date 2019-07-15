class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        # word1 will always be set to the longer of the two words
        if len(word2) > len(word1):
            word1, word2 = word2, word1
        
        matrix = [] 
        
        for i in range(len(word1) + 1):
            row = []
            
            for j in range(len(word2) + 1):
                if i == 0:
                    row.append(j)
                elif j == 0:
                    row.append(i)
                else:
                    if word2[j-1] != word1[i-1]:
                        new_val = min(row[j-1], matrix[i-1][j-1], matrix[i-1][j]) + 1
                    else:
                        new_val = matrix[i-1][j-1]
                        
                    row.append(new_val)
                    
            matrix.append(row)

        return matrix[len(word1)][len(word2)]
                
