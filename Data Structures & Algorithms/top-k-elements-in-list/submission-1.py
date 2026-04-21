from collections import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] +=1
            else:
                dictionary[i] = 1
        sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse = True)
        return [x[0] for x in sorted_dict[:k]]
        
            