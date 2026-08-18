"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        classes = []
        for i in intervals:
            classes.append([i.start,i.end])
        classes.sort()

        i = 1
        while i < len(classes):
            if classes[i-1][1] > classes[i][0]:
                return False

            i+=1

        return True  


