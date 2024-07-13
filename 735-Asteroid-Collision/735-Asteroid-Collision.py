from typing import List
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack.pop()
                if top == -asteroid:
                    asteroid = 0
                elif top > -asteroid:
                    asteroid = top
                else:
                    continue
            if asteroid:
                stack.append(asteroid)

        return list(stack)