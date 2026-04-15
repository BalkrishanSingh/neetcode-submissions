class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        output = {}
        mapping = {letter:i for i,letter in enumerate(alphabet)}
        for i in strs:
            counter = [0 for x in range(26)]
            for j in i:
                counter[mapping[j]] +=1
            tuple_counter = tuple(counter)
            if tuple_counter in output:
                output[tuple_counter].append(i)
            else:
                output[tuple_counter] = [i]
        return list(output.values())
        