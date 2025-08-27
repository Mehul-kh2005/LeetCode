class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)

        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)

        n=n1+n2
        left_half=(n1+n2+1)//2
        low,high=0,n1

        while low<=high:
            mid1=(low+high)//2
            mid2=left_half-mid1

            r1=nums1[mid1] if mid1<n1 else float('inf')
            r2=nums2[mid2] if mid2<n2 else float('inf')
            l1=nums1[mid1-1] if mid1>0 else float('-inf')
            l2=nums2[mid2-1] if mid2>0 else float('-inf')

            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==1:
                    return max(l1,l2)

                else:
                    return (max(l1,l2)+min(r1,r2))/2.0

            elif l1>r2:
                high=mid1-1

            else:
                low=mid1+1