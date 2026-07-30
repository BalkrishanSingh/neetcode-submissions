class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+','-','*','/'}

        for i in tokens:
            if i in operations:
                y = stack.pop()
                x = stack.pop()
                if i in operations - {'/',}:
                    z = eval(x+i+y)
                else:
                    z = int(int(x) / int(y))
                stack.append(str(z))
                continue
            stack.append(i)
                
        return int(stack.pop())
