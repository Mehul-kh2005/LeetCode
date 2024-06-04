class Solution:
    def longestPalindrome(self, s: str) -> int:
        character_set=set()
        length=0

        for char in s:
            if char in character_set:
                character_set.remove(char)
                length+=2
            else:
                character_set.add(char)
        
        if character_set:
            length+=1
        
        return length