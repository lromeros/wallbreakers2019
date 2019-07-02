from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        answer = ''
        freq_s = Counter(s)
        
        for pair in freq_s.most_common(len(s)):
            char = pair[0]
            count = pair[1]
            
            for i in range(pair[1]):
                answer += pair[0]
                
        return answer
