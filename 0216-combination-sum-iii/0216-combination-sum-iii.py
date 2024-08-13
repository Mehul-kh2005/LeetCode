class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr=[num for num in range(1,10)]
        result=combinations(arr,k)
        valid_combinations=[]

        for elements in result:
            if sum(elements)==n:
                valid_combinations.append(list(elements))

        return valid_combinations