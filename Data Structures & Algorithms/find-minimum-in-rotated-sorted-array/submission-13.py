class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)-1

        if nums[left] < nums[right]:
            return nums[left]
        
        


        while left <= right:
            if nums[left] < nums[right]:
                return nums[left]
        
            mid = (left+right)//2
            sLeft = mid-1
            if sLeft < 0:
                sLeft = len(nums)-1
            
            sRight = mid + 1
            if sRight > len(nums) -1:
                sRight = 0
            
            print("mid" + str(mid) + "left" + str(left) + "right" + str(right))
            if nums[mid] <= nums[sLeft] and nums[mid] <= nums[sRight]:
                return nums[mid]
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[mid]
        
                
                
                
        

        