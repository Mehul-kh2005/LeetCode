class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        bannedWords=set(bannedWords)
        return sum(word in bannedWords for word in message)>1