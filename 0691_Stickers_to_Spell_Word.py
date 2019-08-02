class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target_set, remain_set = set(target), set(target)
        char_to_words = collections.defaultdict(set)
        
        for sticker in stickers:
            cleaned = tuple(x for x in sticker if x in target_set)
            sticker_set = set(cleaned)
            
            for c in sticker_set:
                char_to_words[c].add(cleaned)
            
            remain_set -= sticker_set
            
        if remain_set:
            return -1
        
        heap = [(0, len(target), list(target))]
        
        while True:
            used_words, len_target, target = heapq.heappop(heap)
            
            for word in char_to_words[target[0]]:
                new_str = target[:]
                
                for c in word:
                    if c in new_str:
                        new_str.remove(c)
                
                if not new_str:
                    return used_words + 1
                
                heapq.heappush(heap, (used_words + 1, len(new_str), new_str))
