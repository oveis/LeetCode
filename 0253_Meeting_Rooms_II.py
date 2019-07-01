class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sorted_meetings = sorted(intervals, key=lambda inter: inter[0])        
        rooms = []
        
        for meeting in sorted_meetings:
            room_idx = -1
            
            for idx, room in enumerate(rooms):
                if room[1] <= meeting[0]:
                    room_idx = idx
                    break
            
            if room_idx == -1:
                rooms.append(meeting)
            else:
                rooms[room_idx] = meeting
        
        return len(rooms)
