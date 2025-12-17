class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Total number of ways
        count = 1

        # Number of seats in current section
        seats = 0

        # Tracking Index of last S in the previous section
        previous_pair_last = None

        # Keep track of seats in the corridor
        for index, thing in enumerate(corridor):
            if thing == "S":
                seats += 1

                # If two seats, then this is the last S in the section
                # Update seats for the next section
                if seats == 2:
                    previous_pair_last = index
                    seats = 0
                
                # If one seat, then this is the first S in the section
                # Compute the product of non-paired neighbors
                elif seats == 1 and previous_pair_last is not None:
                    count *= (index - previous_pair_last)
                    count %= MOD
        
        # If odd seats, or zero seats
        if seats == 1 or previous_pair_last is None:
            return 0

        # Return the number of ways
        return count
        