class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_length = 0
        current_count = 0
        
        # Initial window
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        
        max_length = current_count
        
        # Slide the window across the string
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_count += 1
            if s[i - k] in vowels:
                current_count -= 1
            max_length = max(max_length, current_count)
        
        return max_length