class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_element = 0
        max_element = 0
        current = 0
        
        for difference in differences:
            current += difference
            min_element = min(min_element, current)
            max_element = max(max_element, current)

        seq_range = max_element - min_element
        total_range = upper - lower

        return max(0, total_range - seq_range + 1)