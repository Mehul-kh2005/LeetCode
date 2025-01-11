class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False

        freq=Counter(s)
        count=0
        for value in freq.values():
            if value%2!=0:
                count+=1

            if count>k:
                return False

        return True        