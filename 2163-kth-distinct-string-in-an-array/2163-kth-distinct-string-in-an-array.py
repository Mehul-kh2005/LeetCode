class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count the frequency of each element
        frequency = Counter(arr)
        
        # Track distinct elements (those with frequency == 1)
        distinct_elements = [item for item in arr if frequency[item] == 1]
        
        # Return the k-th distinct element if it exists, otherwise return an empty string
        if k <= len(distinct_elements):
            return distinct_elements[k - 1]
        return ""