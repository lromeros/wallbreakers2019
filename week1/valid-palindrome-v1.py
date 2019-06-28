class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        
        str_list = [c.lower() for c in s if c.isalnum()]
        end_ptr = len(str_list) - 1
        
        for i in range(math.ceil(len(str_list) / 2)):
            if str_list[i] != str_list[end_ptr - i]:
                return False
    
        return True
