class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls = sum(rolls)
        # Find the remaining sum.
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        # Check if sum is valid or not.
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        # Distribute the remaining mod elements in n_elements list.
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1
        return n_elements