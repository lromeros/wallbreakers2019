class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        upper = len(A)
        lower = 0
        index = math.floor((upper-lower) / 2)
        peak_found = False
        
        while not peak_found:
            left = index - 1 if index - 1 >= 0 else 0
            right = index + 1 if index + 1 < len(A) else len(A)
            
            if A[left] <= A[index] and A[index] >= A[right]:
                peak_found = True
            elif A[left] > A[index]:
                # move down
                upper = index
                index = math.floor(upper / 2)
            else:
                # move up
                lower = index
                index += math.floor((upper - lower) / 2)
            
        return index
