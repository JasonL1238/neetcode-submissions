class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            print(i)
            if not i == "/" and not i == "-" and not i == "*" and not i == "+":
                stack.append(int(i))
            else:
                digit1 = stack.pop()
                digit2 = stack.pop()
                print("1 " + str(digit1))
                print("2 " + str(digit2))

                if i == "/":
                    stack.append(int(digit2/digit1))
                elif i == "-":
                    stack.append(int(digit2-digit1))
                elif i == "+":
                    stack.append(int(digit1+digit2))
                elif i == "*":
                    stack.append(int(digit1*digit2))
        
        return stack[0]