class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()

        for i in range(len(nums)):
            if i>= 1 and nums[i] == nums[i-1]:
                print("skip")
                continue
            
            target = 0 - nums[i]
            pointer1 = i + 1
            pointer2 = len(nums) - 1
            while pointer1 < pointer2:
                if nums[pointer1] + nums[pointer2] == target:
                    output.append([nums[i],nums[pointer1],nums[pointer2]])
                    pointer1 +=1
                    while pointer1 < len(nums) and nums[pointer1] == nums[pointer1-1]:
                        pointer1+=1
                elif nums[pointer1] + nums[pointer2] > target:
                    pointer2 -=1
                else:
                    pointer1 +=1

        return output


        