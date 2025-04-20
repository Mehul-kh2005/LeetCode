class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefix_sum=0
        result=0

        for num in nums:
            prefix_sum+=num

            if prefix_sum-k in freq:
                result+=freq[prefix_sum-k]

            freq[prefix_sum]=freq.get(prefix_sum,0)+1

        return result