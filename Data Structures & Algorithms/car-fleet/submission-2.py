
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position,speed),key = lambda x: x[0],reverse = True)
        stack = []
        for dist,speed in pair:
            time = (target-dist)/speed
            stack.append(time)
            if len(stack)>1 and time <= stack[-2]:
                stack.pop()
           
            
        return len(stack)