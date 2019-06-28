class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        size = len(A)
        result = [0] * size
        e_ind = 0
        o_ind = size - 1
        
        for num in A:
            if num % 2 == 0:
                result[e_ind] = num
                e_ind += 1
            else:
                result[o_ind] = num
                o_ind -= 1
                
        return result 
