class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        
        num_words, unit_words = self.gen_dicts()
        
        units = []
        for i in range(4):
            units.append(num % 1000)
            num /= 1000
        
        total_words = []
        
        for idx, unit_num in enumerate(units):
            if unit_num == 0:
                continue
                
            words = []
            if unit_num >= 100:
                words.append(num_words[unit_num / 100])
                words.append(num_words[100])
                unit_num %= 100
            
            if unit_num in num_words:
                words.append(num_words[unit_num])
            elif unit_num != 0:
                words.append(num_words[unit_num / 10 * 10])
                words.append(num_words[unit_num % 10])
            
            if idx == 0:
                total_words = words
            else:
                total_words = words + [unit_words[1000 ** idx]] + total_words
        
        return ' '.join(total_words)
        
    
    def gen_dicts(self):
        num_words = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            100: 'Hundred'
        }
        
        unit_words = {
            1: '',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }
        
        for i in range(6, 10):
            word = num_words[i]
            word = word[:-1] if word[-1] == 't' else word
            num_words[10 + i] = word + 'teen'
            num_words[10 * i] = word + 'ty'
        
        return num_words, unit_words
