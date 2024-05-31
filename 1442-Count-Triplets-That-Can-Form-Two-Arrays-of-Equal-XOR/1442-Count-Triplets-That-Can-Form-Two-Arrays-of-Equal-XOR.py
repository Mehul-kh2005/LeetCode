class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_XOR = [0] + arr
        size = len(prefix_XOR)
        count = 0

        # Performing XOR operation on the array elements
        for i in range(1, size):
            prefix_XOR[i] ^= prefix_XOR[i - 1]

        # Dictionaries to store counts and totals of XOR values encountered
        count_map = defaultdict(int)
        total_map = defaultdict(int)

        # Iterating through the array
        for i in range(size):
            # Calculating contribution of current element to the result
            count += (
                count_map[prefix_XOR[i]] * (i - 1) - total_map[prefix_XOR[i]]
            )

            # Updating total count of current XOR value
            total_map[prefix_XOR[i]] += i
            count_map[prefix_XOR[i]] += 1

        return count
    
        