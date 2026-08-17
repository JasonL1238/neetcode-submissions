class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1 = 0
        pointer2 = len(s) - 1
        while not s[pointer1].isalnum() :
            pointer1+=1
            if pointer1 > pointer2:
                return True
        while not s[pointer2].isalnum():
            pointer2-=1
            if pointer1 > pointer2:
                return True
        while True:
            print("pointer1 " + str(pointer1))
            print("pointer2 " + str(pointer2))
            if not s[pointer1].lower() == s[pointer2].lower():
                return False
            pointer1+=1
            pointer2-=1
            if pointer1 > pointer2:
                return True
            while not s[pointer1].isalnum():
                pointer1+=1
                if pointer1 > pointer2:
                    return True
            while not s[pointer2].isalnum():
                pointer2-=1
                if pointer1 > pointer2:
                    return True


            
            
        