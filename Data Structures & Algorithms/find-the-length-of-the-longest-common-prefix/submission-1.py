class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        s = set()

        for num in arr1:
            word = str(num)
            for i in range(1,len(word)+1):
                s.add(word[:i])
        longest = 0
        for num in arr2:
            word = str(num)
            for i in range(1,len(word)+1):
                if word[:i] in s:
                    longest= max(longest,i)
        return longest


        



        




        