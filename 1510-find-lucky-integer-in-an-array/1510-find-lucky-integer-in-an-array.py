class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)
        result=-1

        for num,val in freq.items():
            if num==val:
                result=max(result,num)

        return result