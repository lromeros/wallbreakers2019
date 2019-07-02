from collections import Counter

class Solution:
    def formula_counts(self, formula, counter):
        nums = '0123456789'
        atom = ''
        count = ''
        
        for c in formula:
            if c.isupper():
                if len(atom) == 0:
                    atom += c
                else:
                    if count == '':
                        counter[atom] += 1
                        atom = c
                    else:
                        counter[atom] += int(count)
                        atom = c
                        count = ''
            elif c in nums:
                count += c
            else:
                atom += c
        if len(atom) > 0:
            add = int(count) if len(count) > 0 else 1
            counter[atom] += add
            
        return counter
    
    
    def counter_to_string(self, counter):
        answer = []
        for atom in counter.keys():
            count = str(counter.get(atom)) if counter.get(atom) > 1 else ''
            answer.append(atom + str(count))
        answer.sort()            
        return ''.join(answer)
    
    
    def countOfAtoms(self, formula: str) -> str:
        counter = self.formula_counts(formula, Counter())
        return self.counter_to_string(counter)

            
            
