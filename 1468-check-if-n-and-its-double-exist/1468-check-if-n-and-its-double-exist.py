class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_unique=set([arr[0]])

        for num in arr:
            if num*2 in arr_unique or num/2 in arr_unique:
                return True
            arr_unique.add(num)

        return False