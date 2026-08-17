class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        firsts = set()
        prev = set(nums)

        for i in nums:
            if not i-1 in prev:
                firsts.add(i)
        
        largest = 0
        for i in firsts:
            curr = i
            currCount = 0
            while curr in prev:
                currCount += 1
                curr+=1
            largest = max(currCount,largest)
        
        return largest



