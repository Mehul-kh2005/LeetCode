class Solution:
    def primeSubOperation(self, nums):
        max_element = max(nums)

        # Store the sieve array.
        sieve = [1] * (max_element + 1)
        sieve[1] = 0
        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            if sieve[i] == 1:
                for j in range(i * i, max_element + 1, i):
                    sieve[j] = 0

        # Start by storing the currValue as 1, and the initial index as 0.
        curr_value = 1
        i = 0
        while i < len(nums):
            # Store the difference needed to make nums[i] equal to currValue.
            difference = nums[i] - curr_value

            # If difference is less than 0, then nums[i] is already less than
            # currValue. Return false in this case.
            if difference < 0:
                return False

            # If the difference is prime or zero, then nums[i] can be made
            # equal to currValue.
            if sieve[difference] or difference == 0:
                i += 1
                curr_value += 1
            else:
                # Otherwise, try for the next currValue.
                curr_value += 1
        return True