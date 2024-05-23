class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)
        score_copy = score.copy()
       
        # Save the index of each athlete
        score_to_index = defaultdict(int)
        for i in range(N):
            score_to_index[score_copy[i]] = i

        # Sort score copy in descending order
        score_copy.sort(reverse = True)

        # Assign ranks to athletes
        rank = [" "] * N
        for i in range(N):
            if i == 0:
                rank[score_to_index[score_copy[i]]] = "Gold Medal"
            elif i == 1:
                rank[score_to_index[score_copy[i]]] = "Silver Medal"
            elif i == 2:
                rank[score_to_index[score_copy[i]]] = "Bronze Medal"
            else:
                rank[score_to_index[score_copy[i]]] = str(i + 1)

        return rank
   
        