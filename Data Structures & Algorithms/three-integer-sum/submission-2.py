class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        if len(nums) < 3:
            return []
        
        for j in range(0,len(nums)):
            i = 0
            k = len(nums) -1 
            while True:
                if not i<k:
                    break
                if nums[i] + nums[k] == -nums[j] and i != j and j!=k and i!=k:
                    triplet = sorted([nums[i],nums[j], nums[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                    i +=1
                elif nums[i] + nums[k] > -nums[j]:
                    k -= 1
                else:
                    i +=1
                
        return triplets