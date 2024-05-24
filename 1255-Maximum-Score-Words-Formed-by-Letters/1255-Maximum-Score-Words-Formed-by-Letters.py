class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersCounter=Counter(letters)
        totalScore=0

        def explore(index,lettersCounter,currScore):
            nonlocal totalScore

            totalScore=max(totalScore,currScore)
            if index==len(words):
                return
            
            for i in range(index,len(words)):
                tempCounter=copy.deepcopy(lettersCounter)
                word=words[i]
                wordScore=0
                isValid=True

                for char in word:
                    if char in tempCounter and tempCounter[char]>0:
                        tempCounter[char]-=1
                        wordScore+=score[ord(char)-ord('a')]
                    
                    else:
                        isValid=False
                        break
                
                if isValid:
                    explore(i+1,tempCounter,currScore+wordScore)
            
        explore(0,lettersCounter,0)
        return totalScore