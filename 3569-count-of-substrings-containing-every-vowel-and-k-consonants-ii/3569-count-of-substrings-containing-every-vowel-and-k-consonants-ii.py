class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in ["a", "e", "i", "o", "u"]

    def _atLeastK(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = 0
        end = 0
        vowel_count = {}
        consonant_count = 0

        while end < len(word):
            new_letter = word[end]

            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            while len(vowel_count) == 5 and consonant_count >= k:
                num_valid_substrings += len(word) - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] = (
                        vowel_count.get(start_letter) - 1
                    )
                    if vowel_count.get(start_letter) == 0:
                        vowel_count.pop(start_letter)
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_valid_substrings

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)