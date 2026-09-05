class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not len(intervals):
            return [newInterval,]
        result = []
        i = 0
        inserted = False
        while(i<len(intervals) or not inserted):
            #insert new interval while maintaing sorted order
            if not inserted and (not i<len(intervals) or intervals[i][0] > newInterval[0]):
                curr = newInterval
                inserted = True 
            else:
                curr = intervals[i]
                i+=1
            # handle first iteration
            if len(result) == 0:
                result.append(curr)
                continue

            # merge interval else append non overlapping interval
            (a,b) = result[-1]
            (c,d) = curr
            if max(a,c) <= min(b,d):
                result[-1] = [min(a,c),max(b,d)]
            else:
                result.append(curr)
        return result
        
