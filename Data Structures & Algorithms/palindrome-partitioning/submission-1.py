class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        curr = []


        def isPalindrome(pali: str) -> bool:
            print(pali)
            l = 0
            r = len(pali)-1

            while l <= r:
                if not pali[l] == pali[r]:
                    return False
                l += 1
                r -=1
            return True
        
        def search(index:int):
            if index == len(s):
                output.append(curr.copy())
                return
            i = index+1
            while i <= len(s):
                if isPalindrome(s[index:i]):                    
                    curr.append(s[index:i])
                    search(i)
                    curr.pop()
                i +=1

        search(0)
        return output



        