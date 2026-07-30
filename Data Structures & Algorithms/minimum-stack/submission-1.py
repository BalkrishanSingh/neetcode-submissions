class MinStack:

    def __init__(self):
        self.length = 0
        self.stack = []
        self.min_elements = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.length < 1:
            self.min_elements.append(val)
            self.length +=1
            return
        if self.min_elements[-1] < val:
            self.min_elements.append(self.min_elements[-1])
        else:
            self.min_elements.append(val)
        self.length +=1
        
             
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_elements.pop()
        self.length -= 1

        
    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_elements[-1]
        
