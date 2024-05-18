class Solution:
    def search(self, nums, target):
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            #if mid points the target
            if nums[mid]==target:
                return mid
            # if left part is sorted
            if nums[l]<=nums[mid]:
                if nums[l]<=target and target<=nums[mid]:
                    #element exists
                    h=mid-1
                else:
                    #element does not exists
                    l=mid+1
            else:
                if nums[mid]<=target and target<=nums[h]:
                    #element exists
                    l=mid+1
                else:
                    #element does not exists
                    h=mid-1
        return -1 