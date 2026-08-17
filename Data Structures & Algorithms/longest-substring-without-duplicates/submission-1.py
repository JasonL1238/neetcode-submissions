class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        maxLen = 0
        n = len(s)

        left = 0
        right = 0

        while right < n:
            if not s[right] in char:
                char.add(s[right])
                maxLen = max(maxLen,len(char))
                right += 1
            else:
                char.remove(s[left])
                left += 1

        return maxLen
        