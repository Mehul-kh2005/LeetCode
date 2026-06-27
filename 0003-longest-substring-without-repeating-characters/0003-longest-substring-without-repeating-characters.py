class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            # If we have seen the character and it is within our current window, 
            # move the start of the window past the previous occurrence.
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            # Update the latest index of the character
            char_map[char] = end
            
            # Update the maximum length found so far
            max_length = max(max_length, end - start + 1)
            
        return max_length