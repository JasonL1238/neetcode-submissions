class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (right+left)//2
            val = nums[middle]
            if val == target:
                return middle
            valL = nums[left]
            valR = nums[right]
            print("l" + str(left))
            print("r" + str(right))
            if valL <= val:
                if val > target and valL <= target:
                    right = middle-1
                else:
                    left = middle+1
            else:
                if target > val and valR >= target:
                    left = middle +1
                else:
                    right = middle -1
 
        return -1






         

        