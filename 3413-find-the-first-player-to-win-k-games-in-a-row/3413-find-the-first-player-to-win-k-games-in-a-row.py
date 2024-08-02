class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        if k>=len(skills):
            return skills.index(max(skills))

        n=len(skills)
        index_to_skills={idx:val for idx,val in enumerate(skills)}
        count=0
        curr=index_to_skills[0]

        for i in range(1,n):
            if index_to_skills[i]>curr:
                curr=index_to_skills[i]
                count=1
            else:
                count+=1

            if count==k:
                return skills.index(curr)

        return skills.index(curr)