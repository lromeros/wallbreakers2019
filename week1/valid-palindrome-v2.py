class Solution:
    def isPalindrome(self, s: str) -> bool:        
        start = 0
        end = len(s) - 1
        
        while start <= end:
            start_val = s[start].lower()
            end_val = s[end].lower()

            if not start_val.isalnum():
                start += 1
                continue
                
            if not end_val.isalnum():
                end -= 1
                continue 
                
            if start_val != end_val:
                return False
            else:
                start += 1
                end -= 1
            
        return True
