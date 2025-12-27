class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Start with closing at hour 0 and assume the current penalty is 0.
        minPenalty = 0
        curPenalty = 0
        earliestHour = 0

        for i in range(len(customers)):
            ch = customers[i]

            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penatly by 1.
            if ch == "Y":
                curPenalty -= 1
            else:
                curPenalty += 1

            # Update earliestHour if a smaller penatly is encountered.
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty

        return earliestHour
        