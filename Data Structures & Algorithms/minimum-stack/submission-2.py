class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []
    
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minArr.append(val)
        else:
            if self.minArr[-1] < val:
                self.minArr.append(self.minArr[-1])
            else:
                self.minArr.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minArr.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
