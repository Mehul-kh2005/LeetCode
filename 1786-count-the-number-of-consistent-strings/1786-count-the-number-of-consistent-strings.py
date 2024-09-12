class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        count=0

        for word in words:
            if all(char in allowed for char in word):
                count+=1

        return count