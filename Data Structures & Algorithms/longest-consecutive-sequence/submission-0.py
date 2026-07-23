class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        L = set(nums)
        max_streak = 0
        for i in L:
            if i - 1 not in L:
                curr = i + 1
                streak = 1
                while(curr in L ):
                    streak += 1
                    curr += 1
                if max_streak < streak:
                    max_streak = streak
        return max_streak
