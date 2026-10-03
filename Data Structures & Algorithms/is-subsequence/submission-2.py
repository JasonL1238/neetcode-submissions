class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == 0:
            return True
            
        index = 0

        for i in t:
            if s[index] == i:
                index += 1
                if index >= len(s):
                    return True
        
        return index == len(s)