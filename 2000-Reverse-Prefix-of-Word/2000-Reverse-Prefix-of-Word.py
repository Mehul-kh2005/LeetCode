class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            index=word.index(ch)
            return word[index::-1]+word[index+1:]
        return word