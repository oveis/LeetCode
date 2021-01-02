class Solution:

    def __init__(self, w: List[int]):
        sum_w = sum(w)
        self._prob = []
        for idx, weight in enumerate(w):
            if idx == 0:
                self._prob.append(weight/sum_w)
            else:
                self._prob.append(self._prob[-1] + weight/sum_w)
        

    def pickIndex(self) -> int:
        r = random.random()
        for idx, prob in enumerate(self._prob):
            if r <= prob:
                return idx
        
        return len(self._prob) - 1
