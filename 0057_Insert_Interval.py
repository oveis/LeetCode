class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        
        for idx, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                intervals.insert(idx, newInterval)
                break
            elif idx == len(intervals) -1:
                intervals.append(newInterval)
                break
        
        ans = [intervals[0]]
        for interval in intervals[1:]:
            if ans[-1][1] >= interval[0]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        
        return ans
