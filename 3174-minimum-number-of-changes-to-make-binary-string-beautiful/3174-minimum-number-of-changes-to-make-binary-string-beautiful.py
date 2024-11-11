class Solution:

    def minChanges(self, s: str) -> int:

        min_changes_required = 0

        # Check pairs of characters (i, i+1) with step size 2

        for i in range(0, len(s), 2):

            # If characters in current pair don't match,

            # we need one change to make them equal

            if s[i] != s[i + 1]:

                min_changes_required += 1

        return min_changes_required




