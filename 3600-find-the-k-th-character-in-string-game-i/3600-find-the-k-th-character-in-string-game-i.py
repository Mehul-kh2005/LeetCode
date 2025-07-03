class Solution:
    def kthCharacter(self, k: int) -> str:
        result="a"
        
        while len(result)<k:
            curr=""
            for ch in result:
                next_ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
                curr += ch + next_ch

            result=curr

        return result[k-1]