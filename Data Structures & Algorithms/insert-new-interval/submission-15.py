class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        added = False
        
        if not added and newInterval[0] <= intervals[0][0]:
            if newInterval[1] >= intervals[i][0]:
                intervals[0][0] = min(newInterval[0],intervals[0][0])
                intervals[0][1] = max(newInterval[1],intervals[0][1])
                added = True
            else:
                intervals.insert(0,newInterval)
                added = True

        while i<len(intervals):
            if not added and newInterval[0] >= intervals[i][0]:
                if newInterval[0] <= intervals[i][1]:
                    intervals[i][1] = max(newInterval[1],intervals[i][1])
                    added = True
                elif i == len(intervals)-1 or newInterval[0] <= intervals[i+1][0]: 
                    intervals.insert(i+1,newInterval)
                    added = True
            
            if i > 0 and intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
                intervals.pop(i)
                i-=1
            i+=1
 
        return intervals


            

