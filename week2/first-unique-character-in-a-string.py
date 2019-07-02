class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freqs = {}
        lowest_i = len(s)
        
        for i in range(len(s)):
            if char_freqs.get(s[i]) is None:
                char_freqs[s[i]] = {'first_index':i, 'counter':1}
            else:
                char_freqs.get(s[i])['counter'] += 1
        for d in char_freqs.values():
            if d['counter'] == 1 and d['first_index'] < lowest_i:
                lowest_i = d['first_index']
                
        if lowest_i < len(s):
            return lowest_i
        else:
            return -1
        
