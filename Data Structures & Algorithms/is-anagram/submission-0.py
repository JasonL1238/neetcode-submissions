class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        first = [0]* 26
        second = [0]* 26

        for i in range(len(s)):
            index1 = ord(s[i]) - ord('a')
            index2 = ord(t[i]) - ord('a')

            first[index1] += 1
            second[index2] +=1

        return first == second