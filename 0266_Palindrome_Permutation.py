class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        odd_count = sum([1 for num in count.values() if num % 2 == 1])
        return odd_count <= 1
