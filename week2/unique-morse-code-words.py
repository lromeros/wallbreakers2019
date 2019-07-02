class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_mappings = dict(zip([chr(i) for i in range(97, 124)], [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        mappings_seen = {}
        unique = 0
        
        for word in words:
            morse = ''
            for l in word:
                morse += morse_mappings.get(l)
            if mappings_seen.get(morse) is None:
                mappings_seen[morse] = 1
                unique += 1
                
        return unique 
                
