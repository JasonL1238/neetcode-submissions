class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        numzeroes = 0
        for i in nums:
            if not i == 0:
                    total *= i
            else:
                numzeroes +=1

        
        output = []
        for i in nums:
            if numzeroes >= 2:
                output.append(0)
            elif numzeroes < 1:
                output.append(int(total/i))
            else:
                if i == 0:
                    output.append(int(total))
                else:
                    output.append(0)
        
        return output
        