class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,1
        if s == "":
            return 0
        InSet = {s[0],}
        streak = 1
        while j < len(s):
            
            while s[j] in InSet and i<j:
                InSet.discard(s[i])
                i+=1
            streak = max(len(InSet)+1,streak)
            InSet.add(s[j])
            j+=1
        return streak
        