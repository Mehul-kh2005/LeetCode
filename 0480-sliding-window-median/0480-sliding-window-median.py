class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = sorted(nums[:k])
        
        for i in range(k, len(nums) + 1):

            result.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)
            
            if i == len(nums):
                break
            
            window.remove(nums[i - k])
            bisect.insort(window, nums[i])

        return result