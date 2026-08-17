class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        m = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }

        if len(digits) == 0:
            return []

        curr = []
        output = []

        def search(index:int):

            if index == len(digits):
                output.append("".join(curr.copy()))
                return 

            i = m[int(digits[index])]
            for k in i:
                curr.append(k)
                search(index+1)
                curr.pop()
        
        search(0)
        return output
                