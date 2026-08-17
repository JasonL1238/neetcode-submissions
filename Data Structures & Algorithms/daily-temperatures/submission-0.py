class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        stack.append((temperatures[0],0))
        print(stack)

        for i in range(len(temperatures)):
            if i == 0:
                continue
            curr = temperatures[i]
            top = stack[-1]
            while not len(stack) == 0 and top[0] < curr:
                popped = stack.pop()
                index = top[1]
                print(stack)
                print(top)
                print(index)
                output[index] = i - index
                if not len(stack) == 0:
                    top = stack[-1]
            stack.append((curr,i))
        
        return output


