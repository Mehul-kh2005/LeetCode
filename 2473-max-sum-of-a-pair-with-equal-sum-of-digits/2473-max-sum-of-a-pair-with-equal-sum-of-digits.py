from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map=defaultdict(list)

        for num in nums:
            digit_sum=sum(int(digit) for digit in str(num))
            digit_sum_map[digit_sum].append(num)

        max_sum=-1
        for num_list in digit_sum_map.values():
            if len(num_list)>=2:
                num_list.sort(reverse=True)
                max_sum=max(max_sum,num_list[0]+num_list[1])

        return max_sum