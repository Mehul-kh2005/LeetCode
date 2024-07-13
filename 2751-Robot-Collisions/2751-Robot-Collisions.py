class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n=len(positions)
        indices=list(range(n))
        result=[]
        stack=deque()

        indices.sort(key=lambda x: positions[x])

        for curr_index in indices:

            if directions[curr_index]=='R':
                stack.append(curr_index)
            
            else:
                while stack and healths[curr_index]>0:
                    top_index=stack.pop()

                    if healths[top_index]>healths[curr_index]:
                        healths[top_index]-=1
                        stack.append(top_index)
                        healths[curr_index]=0
                    
                    elif healths[top_index]<healths[curr_index]:
                        healths[top_index]=0
                        healths[curr_index]-=1
                    
                    else:
                        healths[top_index]=0
                        healths[curr_index]=0

        for health in healths:
            if health>0:
                result.append(health)
        
        return result