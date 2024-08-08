class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)

        if len_p > len_s:
            return []

        # Count frequency of characters in p
        p_count = Counter(p)
        
        # Count frequency of characters in the initial window of s
        s_count = Counter(s[:len_p])
        
        result = []

        # Check if initial window is an anagram
        if s_count == p_count:
            result.append(0)
        
        # Slide the window across s
        for i in range(1, len_s - len_p + 1):
            # Remove the character going out of the window
            s_count[s[i - 1]] -= 1
            if s_count[s[i - 1]] == 0:
                del s_count[s[i - 1]]
            
            # Add the new character coming into the window
            s_count[s[i + len_p - 1]] += 1
            
            # Compare frequency counts
            if s_count == p_count:
                result.append(i)
        
        return result