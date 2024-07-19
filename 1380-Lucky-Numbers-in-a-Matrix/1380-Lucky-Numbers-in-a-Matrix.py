class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Find the minimum value in each row
        min_values_per_row = [min(row) for row in matrix]
        
        # Find the maximum value in each column
        max_values_per_column = [max(col) for col in zip(*matrix)]
        
        # Find common elements between min values of rows and max values of columns
        return list(set(min_values_per_row).intersection(set(max_values_per_column)))