class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]

        while not slow == fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        print(slow)
        print(fast)
        
        slow = nums[0]
        print(slow)


        while not slow == fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
