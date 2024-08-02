class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>len(arr):
            return max(arr)

        count=0
        curr=arr[0]
        for i in range(1, len(arr)):
            if arr[i] > curr:
                curr = arr[i]
                count = 1
            else:
                count += 1
            
            # If count reaches k, the current winner has won k consecutive comparisons
            if count == k:
                return curr

        return curr