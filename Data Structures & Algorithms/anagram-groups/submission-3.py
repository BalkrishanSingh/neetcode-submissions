class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        output = {}
        for i in strs:
            counter = [0]*26
            for j in i:
                counter[ord(j)-ord('a')] +=1
            tuple_counter = tuple(counter)
            if tuple_counter in output:
                output[tuple_counter].append(i)
            else:
                output[tuple_counter] = [i]
        return list(output.values())
        