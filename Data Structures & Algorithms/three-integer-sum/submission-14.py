class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        if len(nums) < 3:
            return []
        
        for j,a in enumerate(nums):
            if a >0:
                break
            if a == nums[j-1] and j>0:
                continue

            i = j+1
            k = len(nums) -1 
            while i<k:
                if nums[i] + nums[k] == -nums[j] and i != j and j!=k and i!=k:
                    triplet = ([nums[i],nums[j], nums[k]])
                    triplets.append(triplet) 
                    i+=1
                    k-=1
                    while nums[i] == nums[i-1] and i < k:
                        i+=1   
                elif nums[i] + nums[k] > -nums[j]:
                    k -= 1
                else:
                    i +=1
                
        return triplets