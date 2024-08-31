class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s or len(s) == 1:
            return False
    
        doubled_s = s + s
        modified_s = doubled_s[1:-1]

        return s in modified_s