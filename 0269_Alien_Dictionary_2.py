class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjacent = defaultdict(set)
        indepth = {c: 0 for word in words for c in word}
        
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adjacent[c]:
                        adjacent[c].add(d)
                        indepth[d] += 1
                    break
            else:
                if len(first_word) > len(second_word):
                    return ''
        
        ans = []
        
        queue = deque([c for c in indepth if indepth[c] == 0])
        
        while queue:
            c = queue.popleft()
            ans.append(c)
            
            for d in adjacent[c]:
                indepth[d] -= 1
                if indepth[d] == 0:
                    queue.append(d)
                 
        if len(ans) != len(indepth):
            return ''
        
        return ''.join(ans)
