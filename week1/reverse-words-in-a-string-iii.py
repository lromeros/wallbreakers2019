class Solution:
    def reverse_string(self, word):
        reverse = ''
        
        for i in range(len(word)):
            c = word[len(word) - 1 - i]
            reverse += c
            
        return reverse
    
    
    def reverseWords(self, s: str) -> str:
        words = s.split()
        answer = ""
        
        for word in words:
            answer += self.reverse_string(word)
            answer += ' '
            
        return answer[0:len(answer) - 1]
