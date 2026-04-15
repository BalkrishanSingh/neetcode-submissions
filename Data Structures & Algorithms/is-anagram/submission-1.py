class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A:[str,int] = {}
        B:[str,int] = {}
        for i in s:
            if i in A.keys():
                A[i] +=1
            else:
                A[i] = 1
        for i in t:
            if i in B.keys():
                B[i] +=1
            else:
                B[i] = 1
        return A == B