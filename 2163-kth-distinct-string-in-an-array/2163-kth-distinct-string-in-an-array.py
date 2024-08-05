class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=0
        for char in arr:
            if arr.count(char)==1:
                count+=1
            if count==k:
                return char
        return ""