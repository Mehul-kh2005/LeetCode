class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n=len(nums)
        product_freq={}
        num_tuples=0

        for i in range(n):
            for j in range(i+1,n):
                product=nums[i]*nums[j]
                product_freq[product]=product_freq.get(product,0)+1

        for freq in product_freq.values():
            pairsOfEqualProduct=((freq-1)*freq)//2
            num_tuples+=pairsOfEqualProduct*8

        return num_tuples