class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_sum=0
        negative_count=0
        n=len(matrix)
        smallest_value=float('inf')

        for i in range(n):
            for j in range(n):
                matrix_sum+=abs(matrix[i][j])
                smallest_value=min(smallest_value,abs(matrix[i][j]))
                if matrix[i][j]<0:
                    negative_count+=1

        if negative_count%2==0:
            return matrix_sum
        else:
            return matrix_sum-2*smallest_value