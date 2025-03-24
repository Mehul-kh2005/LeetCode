class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        latestEnd=0
        count=0
        meetings.sort()

        for start,end in meetings:
            if start>latestEnd+1:
                count+=start-latestEnd-1
            
            latestEnd=max(latestEnd,end)

        if latestEnd!=days:
            count+=days-latestEnd

        return count