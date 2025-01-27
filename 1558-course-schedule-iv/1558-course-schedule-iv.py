class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        is_prerequisite=[[False for _ in range(numCourses)] for _ in range(numCourses)]

        for i,j in prerequisites:
            is_prerequisite[i][j]=True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    is_prerequisite[src][target]=is_prerequisite[src][target] or (is_prerequisite[src][intermediate] and is_prerequisite[intermediate][target])

        result=[]
        for query in queries:
            result.append(is_prerequisite[query[0]][query[1]])

        return result