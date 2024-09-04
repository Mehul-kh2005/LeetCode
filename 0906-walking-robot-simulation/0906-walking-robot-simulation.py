class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set=set(map(tuple,obstacles))
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        x,y,direction=0,0,0
        max_distance=0

        for command in commands:
            if command==-1:
                direction=(direction+1)%4

            elif command==-2:
                direction=(direction+3)%4

            else:
                for _ in range(command):
                    new_x,new_y=x+directions[direction][0],y+directions[direction][1]

                    if (new_x,new_y) not in obstacle_set:
                        x,y=new_x,new_y
                        max_distance=max(max_distance,x*x+y*y)

                    else:
                        break

        return max_distance