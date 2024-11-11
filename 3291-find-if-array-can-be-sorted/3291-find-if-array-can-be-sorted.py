class Solution:

    def canSortArray(self, nums):

        # Number of set bits of the elements in the current segment

        num_of_set_bits = bin(nums[0]).count("1")

        max_of_segment = nums[0]

        min_of_segment = nums[0]

        # Initialize max of the previous segment to the smallest possible integer

        max_of_prev_segment = float("-inf")

        for i in range(1, len(nums)):

            if bin(nums[i]).count("1") == num_of_set_bits:

                # Element belongs to the same segment

                # Update min and max values of the segment

                max_of_segment = max(max_of_segment, nums[i])

                min_of_segment = min(min_of_segment, nums[i])

            else:  # Element belongs to a new segment

                # Check if the segments are arranged properly

                if min_of_segment < max_of_prev_segment:

                    return False

                # Update the previous segment's max

                max_of_prev_segment = max_of_segment

                # Start a new segment with the current element

                max_of_segment = nums[i]

                min_of_segment = nums[i]

                num_of_set_bits = bin(nums[i]).count("1")

        # Final check for proper segment arrangement

        if min_of_segment < max_of_prev_segment:

            return False

        return True
   
        