class Solution:
    def arrangeWords(self, text: str) -> str:
        words=text.lower().split()
        words.sort(key=len)
        return " ".join(words).capitalize()
