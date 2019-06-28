class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                val = A[i][len(A[i]) - 1 - j]
                new_val = 0 if val == 1 else 1
                row.append(new_val)
            A[i] = row
        return A
