class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = dict()
        cache[0] = 1

        for i in nums:
            new = dict()
            for key in list(cache.keys()):
                p = key + i
                n = key - i

                if not p in new:
                    new[p] = 0
                new[p] += cache[key]
                if not n in new:
                    new[n] = 0
                new[n] += cache[key]

            cache = new

        
        if target in cache:
            return cache[target]
        return 0

