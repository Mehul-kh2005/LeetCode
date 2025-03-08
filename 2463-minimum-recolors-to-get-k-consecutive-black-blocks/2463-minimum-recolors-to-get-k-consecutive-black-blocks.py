class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window=[]
        ans=float("inf")

        for i in range(0,len(blocks)-k+1):
            window=blocks[i:i+k]
            print(window)
            ans=min(ans,window.count("W"))

        return ans