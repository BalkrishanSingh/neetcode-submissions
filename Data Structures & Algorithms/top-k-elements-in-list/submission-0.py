from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = Counter(nums)
        most_common_k = arr.most_common(k)
        return [x for x,_ in most_common_k]
            