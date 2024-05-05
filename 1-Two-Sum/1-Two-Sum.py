class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            complement = target-nums[i]
            #check if the complement exists in the hashmap
            if complement in hashmap:
                return [hashmap[complement],i]  #return the indices of the 2 elements that sum up to the target
            
            hashmap[nums[i]]=i   #otherwise, store the current element and its index in the hashmap
        return []