class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]]+[words[i] for i in range(1,len(groups)) if groups[i]!=groups[i-1]]