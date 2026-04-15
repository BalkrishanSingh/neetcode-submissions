class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i,num in enumerate(nums):
            difference = target - num
            if difference in HashMap:
                return list((HashMap[difference],i))
            HashMap[num] = i
        return [-1,-1]

           