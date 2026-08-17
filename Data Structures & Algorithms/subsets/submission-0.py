class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = [[]]

        for i in nums:

            l = len(output)

            for k in range(l):

                new = output[k].copy()
                new.append(i)
                output.append(new)
        
        return output
