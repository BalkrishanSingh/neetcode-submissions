import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(piles,h,k):
            i = 0
            required_h = 0
            for i in piles:
                required_h += math.ceil(i/k)
               
            return required_h <= h
            

        left = 1
        right = 1000000000
        smallest_k = 1
        while left <= right:
            mid = (left+(right-left)//2)
            if isValid(piles,h,mid):
                smallest_k = mid
                right = mid - 1
            else:
                left = mid +1
        return smallest_k


