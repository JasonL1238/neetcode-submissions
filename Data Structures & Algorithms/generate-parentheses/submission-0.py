class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        curr = []

        def depth(a:int, b:int):

            if b < 1 and a > 0:
                curr.append("(")
                depth(a-1,b+1)  
                curr.pop()
            elif a < 1 and b > 0:
                curr.append(")")
                depth(a,b-1)
                curr.pop()
            elif a > 0 and b > 0:
                curr.append("(")
                depth(a-1,b+1)
                curr.pop()
                curr.append(")")
                depth(a,b-1)
                curr.pop()
            else:
                output.append("".join(curr.copy()))
        
        depth(n,0)

        return output
                
