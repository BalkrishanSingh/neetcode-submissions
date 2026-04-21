class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in strs:
            encoded_string += chr(len(i))
            encoded_string += i
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        if len(s) == 0:
            return []
        current_str_remaining_count = ord(s[0])
        current_str = ""
        for i,letter in enumerate(s[1:]):
            if current_str_remaining_count != 0:
                current_str += letter
                current_str_remaining_count -=1
            else:
                current_str_remaining_count = ord(letter)
                decoded_list.append(current_str)
                current_str = ""
            
        return decoded_list+[current_str]