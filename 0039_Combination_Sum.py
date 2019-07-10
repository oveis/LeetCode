class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.combine_candidates([], candidates, 0, target, ans)
        return ans
        
        
    def combine_candidates(self, cur_ans, candidates, pos, target, ans):
        if target == 0:
            ans.append(cur_ans)
        elif target > 0 and pos < len(candidates):
            self.combine_candidates(cur_ans, candidates, pos + 1, target, ans)
            
            num = candidates[pos]
            self.combine_candidates(cur_ans + [num], candidates, pos, target - num, ans)
