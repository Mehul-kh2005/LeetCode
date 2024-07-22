class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs=0
        num_set=set()
        for num in nums:
            n=nums.count(num)
            if n>1 and num not in num_set:
                pairs+=(n*(n-1))//2
                num_set.add(num)

        return pairs