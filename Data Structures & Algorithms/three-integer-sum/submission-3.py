class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = dict()

        nums.sort()

        for i in range(len(nums)):
            target = 0 - nums[i]
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            while pointer1 < pointer2:
                if nums[pointer1] + nums[pointer2] == target:
                    index = tuple([nums[i],nums[pointer1],nums[pointer2]])
                    if not index in output:
                        output[index] = [nums[i],nums[pointer1],nums[pointer2]]
                    pointer1 +=1
                elif nums[pointer1] + nums[pointer2] > target:
                    pointer2 -=1
                else:
                    pointer1 +=1

        return list(output.values())


        