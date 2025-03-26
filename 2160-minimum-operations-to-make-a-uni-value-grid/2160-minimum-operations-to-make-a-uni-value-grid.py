class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums_list=[]
        result=0

        for row in grid:
            for num in row:
                nums_list.append(num)

        nums_list.sort()
        length=len(nums_list)

        median_element=nums_list[length//2]

        for num in nums_list:
            if (num-median_element)%x!=0:
                return -1

            result+=abs(median_element-num)//x

        return result