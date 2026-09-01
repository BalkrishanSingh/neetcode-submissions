class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        arr = [0]*26
        left = 0
        max_sequence = 1
        most_freq = 0

        for right,char in enumerate(s):
            char_index = ord(char) - ord('A')
            if left > right:
                break
            arr[char_index] += 1
            most_freq = max(most_freq,arr[char_index])
            unsimilar = (right-left+1) - most_freq
            if unsimilar > k:
                left_char_index = ord(s[left]) - ord('A')
                arr[left_char_index] -= 1
                left += 1
            max_sequence = max(max_sequence,(right-left+1))
        return max_sequence

            