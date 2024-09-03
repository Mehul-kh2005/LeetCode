import bisect
from collections import deque

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = deque()
        self.sorted_nums = []

    def addElement(self, num: int) -> None:
        # Add the new element to the deque
        self.nums.append(num)
        # Insert the new element into the sorted list
        bisect.insort(self.sorted_nums, num)
        
        # Ensure that the deque only contains the last m elements
        if len(self.nums) > self.m:
            old_num = self.nums.popleft()
            # Remove old_num from the sorted list
            index = bisect.bisect_left(self.sorted_nums, old_num)
            self.sorted_nums.pop(index)
        
    def calculateMKAverage(self) -> int:
        # Check if the number of elements is less than m
        if len(self.nums) < self.m:
            return -1
        
        # Calculate the sum of the middle elements
        start = self.k
        end = self.m - self.k
        total = sum(self.sorted_nums[start:end])
        
        # Calculate and return the average rounded down
        return total // (self.m - 2 * self.k)

# Example usage:
# obj = MKAverage(3, 1)
# obj.addElement(3)
# obj.addElement(1)
# print(obj.calculateMKAverage())  # Output: -1
# obj.addElement(10)
# obj.addElement(5)
# print(obj.calculateMKAverage())  # Output: 3
# obj.addElement(5)
# print(obj.calculateMKAverage())  # Output: 5