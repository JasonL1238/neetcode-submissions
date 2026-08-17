class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        i = 0
        added = False
        intervals.sort()
        
        while i<len(intervals):
            if len(stack) == 0 or stack[-1][1] < intervals[i][0]:
                stack.append(intervals[i])
            else: 
                prev = stack.pop()
                new = [min(prev[0],intervals[i][0]),max(intervals[i][1],prev[1])]
                stack.append(new)
            

            i+=1
            
        return stack