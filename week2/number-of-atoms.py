from collections import Counter

class Formula:
    def __init__(self, string):
        self.formula = string
        self.index = 0
        self.prior_index = 0
    
    def rewind(self):
        self.index = self.prior_index
    
    def get_next_token(self):
        self.prior_index = self.index
        
        token = ''
        
        for i in range(self.index, len(self.formula)):
            c = self.formula[i]
            
            if len(token) == 0:
                token += c
            elif c in ['(', ')'] or c.isupper():
                self.index = i
                break
            elif c.isnumeric():
                if token.isnumeric():
                    token += c
                else:
                    self.index = i
                    break
            else:
                token += c
            
            if i == len(self.formula) - 1:
                self.index = len(self.formula)
            
        return token    
 
        
class Solution:

    def multiply_counter(self, counter, mult):
        for key in counter.keys():
            counter[key] *= mult
        
    def formula_counts(self, tokenizer):
        counter = Counter()
        token = tokenizer.get_next_token()
        
        while token != '':
            if token.isalpha():
                next_token = tokenizer.get_next_token()
                if next_token.isnumeric():
                    counter[token] += int(next_token)
                    token = tokenizer.get_next_token()
                else:
                    counter[token] += 1
                    token = next_token
            elif token == '(':
                counter += self.formula_counts(tokenizer)
                token = tokenizer.get_next_token()
            elif token == ')':
                next_token = tokenizer.get_next_token()
                if next_token.isnumeric():
                    self.multiply_counter(counter, int(next_token))
                else:
                    tokenizer.rewind()
                break
        
        return counter
    
    
    def counter_to_string(self, counter):
        answer = []
        for atom in counter.keys():
            count = str(counter.get(atom)) if counter.get(atom) > 1 else ''
            answer.append(atom + str(count))
        answer.sort()            
        return ''.join(answer)
    
    
    def countOfAtoms(self, formula: str) -> str:
        tokenizer = Formula(formula)
        counter = self.formula_counts(tokenizer)
        return self.counter_to_string(counter)

