class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = int(len(nums)/2)
        left = 0
        right = len(nums)-1

        while True:
            num = nums[i]
            if num == target:
                return i
            elif num > target:
                if right == left:
                    return -1
                right = i - 1
                i = int((right+left)/2)
            else:
                if right == left:
                    return -1
                left = i + 1
                i = int((right+left)/2)

        

        