class Solution:
    def sortVowels(self, s: str) -> str:
        vowelsSet=set('AEIOUaeiou')
        vowels=sorted([char for char in s if char in vowelsSet])

        result=[]
        it=iter(vowels)

        for char in s:
            result.append(next(it) if char in vowelsSet else char)

        return "".join(result)