"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0:
            return 0

        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s = 0
        e = 0
        curr = 0
        m = 1

        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                curr +=1
                m = max(m,curr)
            else:
                e+=1
                curr -=1


        return m
            


