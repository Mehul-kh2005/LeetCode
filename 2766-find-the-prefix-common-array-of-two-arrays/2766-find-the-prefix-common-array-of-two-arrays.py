class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)

        prefix_common_array = [0 for _ in range(n)]

        frequency = [0 for _ in range(n + 1)]

        common_count = 0

        # Iterate through the elements of both arrays

        for current_index in range(n):

            # Increment frequency of current elements in A and B

            # Check if the element in A has appeared before (common in prefix)

            frequency[A[current_index]] += 1

            if frequency[A[current_index]] == 2:

                common_count += 1

            # Check if the element in B has appeared before (common in prefix)

            frequency[B[current_index]] += 1

            if frequency[B[current_index]] == 2:

                common_count += 1

            # Store the count of common elements for the current prefix

            prefix_common_array[current_index] = common_count

        # Return the final array with counts of common elements in each prefix

        return prefix_common_array
 
        