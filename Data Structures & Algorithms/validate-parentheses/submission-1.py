class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                opening = stack.pop()
                if (i == ")" and opening == "(") or (i == "]" and opening == "[") or (i == "}" and opening == "{"): 
                    continue
                else:
                    return False
        
        return len(stack) == 0
                