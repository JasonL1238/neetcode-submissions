class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        stack = []
        count = 0
        stack.append(intervals[0])

        print(intervals)

        i = 1

        while i < len(intervals):
            top = stack[-1]
            if top[1] > intervals[i][0]:
                if top[1] > intervals[i][1]:
                    stack.pop()
                    stack.append(intervals[i])
                count += 1
            else:
                stack.append(intervals[i])
            i+=1
        
        return count
            