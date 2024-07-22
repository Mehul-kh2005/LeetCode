class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        heightToNameMap=dict(zip(heights,names))
        heights=sorted(heights,reverse=True)
        names=[heightToNameMap[height] for height in heights]

        return names