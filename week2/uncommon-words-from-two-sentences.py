class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split()
        B = B.split()
        word_freqs = {}
        
        for i in range(len(A)):
            word_freqs[A[i]] = word_freqs.get(A[i], 0) + 1
        for i in range(len(B)):
            word_freqs[B[i]] = word_freqs.get(B[i], 0) + 1
                
        return [w for w, count in word_freqs.items() if count == 1]
