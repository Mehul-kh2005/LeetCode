class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        unique_substrings = set()

        def backtrack(start):
            if start==len(s):
                return 0

            max_split=0

            for end in range(start+1,len(s)+1):
                substring=s[start:end]

                if substring not in unique_substrings:
                    unique_substrings.add(substring)
                    max_split=max(max_split,1+backtrack(end))

                    unique_substrings.remove(substring)

            return max_split

        return backtrack(0)