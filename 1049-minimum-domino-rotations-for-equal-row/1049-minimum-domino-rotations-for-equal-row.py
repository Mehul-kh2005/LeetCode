class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target: int) -> int:
            tops_count=bottoms_count=0

            for i in range(n):
                if tops[i]!=target and bottoms[i]!=target:
                    return float('inf')

                elif tops[i]!=target:
                    tops_count+=1

                elif bottoms[i]!=target:
                    bottoms_count+=1

            return min(tops_count,bottoms_count)

        n=len(tops)
        result=min(check(tops[0]),check(bottoms[0]))

        return result if result!=float('inf') else -1