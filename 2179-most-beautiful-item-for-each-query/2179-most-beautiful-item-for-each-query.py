class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0])

        max_beauty=items[0][1]
        for i in range(1,len(items)):
            max_beauty=max(max_beauty,items[i][1])
            items[i][1]=max_beauty

        return [self.binary_search(items,q) for q in queries]

    def binary_search(self,items,price):
        left,right=0,len(items)-1
        max_beauty=0

        while left<=right:
            mid=(left+right)//2
            if items[mid][0]>price:
                right=mid-1

            else:
                max_beauty=max(max_beauty,items[mid][1])
                left=mid+1

        return max_beauty