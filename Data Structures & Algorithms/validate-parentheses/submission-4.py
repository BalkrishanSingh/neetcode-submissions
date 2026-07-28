class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        D = {')':'(','}':'{',']':'['}
        for i in s:
            if i in {'(','{','['}:
                S.append(i)
            if i in {')','}', ']'}:
                if not S or S.pop() != D[i]:
                   return False
        return True and not S
            