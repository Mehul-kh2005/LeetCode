from bisect import insort

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        arr=[]
        for num in nums:
            insort(arr,num)
        median=arr[len(arr)//2]
        return sum(abs(median-num) for num in arr)