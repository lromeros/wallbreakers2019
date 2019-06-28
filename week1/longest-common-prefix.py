class Solution:
    def find_length_of_smallest_str(self, strs):
        min_len = float('Inf')
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        return min_len
        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = [list(s) for s in strs]
        prefix = ''
        search_range = self.find_length_of_smallest_str(strs) if len(strs) > 0 else 0
        
        for i in range(search_range):
            letter = ''
            for j in range(len(strs)):
                if letter == '':
                    letter = strs[j][i]
                else:
                    if letter != strs[j][i]:
                        letter = '-'
                        break
            if letter == '-':
                break
            else:
                prefix += letter
        return prefix
