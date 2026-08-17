class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums.sort()
        total = set(nums)
        print(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            index1 = 0
            index2 = len(nums) -1
            while index1 < i and index2 > i:
                
                if nums[index1] + nums[index2] > target:
                    index2 -=1
                elif nums[index1] + nums[index2 ] < target:
                    index1 +=1
                else:
                    arr = sorted([nums[i],nums[index1],nums[index2]])

                    if arr not in output:
                        output.append(arr)

                    index1+=1

            
            

        return output

        