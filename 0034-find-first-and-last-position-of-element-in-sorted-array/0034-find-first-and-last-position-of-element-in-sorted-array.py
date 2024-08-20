class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums,target,findFirst):
            low,high=0,len(nums)-1
            result=-1

            while low<=high:
                mid=(low+high)//2

                if nums[mid]==target:
                    result=mid
                    if findFirst:
                        high=mid-1
                    else:
                        low=mid+1
                
                elif nums[mid]<target:
                    low=mid+1

                else:
                    high=mid-1

            return result

        first=binarySearch(nums,target,True)
        last=binarySearch(nums,target,False)
        return [first,last]