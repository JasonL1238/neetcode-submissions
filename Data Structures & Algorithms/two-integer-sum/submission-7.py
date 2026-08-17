class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
                d[target-nums[i]] = i


        print(d)
        
        for i in range(len(nums)):
            if nums[i] in d and i != d[nums[i]]:
                return [i,d[nums[i]]]