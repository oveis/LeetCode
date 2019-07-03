class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda interval: interval[0])
        
        for idx in range(1, len(intervals)):
            if intervals[idx-1][1] > intervals[idx][0]:
                return False
        
        return True
