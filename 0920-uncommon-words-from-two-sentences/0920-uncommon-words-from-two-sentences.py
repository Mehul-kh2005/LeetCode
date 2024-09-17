class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count = Counter(s1.split()) + Counter(s2.split())
        return [word for word,count in word_count.items() if count==1]