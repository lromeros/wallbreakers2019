class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fb_dict = {3:'Fizz', 5:'Buzz'}
        answers = []
        for num in range(1, n+1):
            val = ''
            for key in fb_dict.keys():
                if num % key == 0:
                    val += fb_dict.get(key)
            if val == '':
                val = str(num)
            answers.append(val)
        return answers
