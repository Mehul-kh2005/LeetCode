class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []

        for current_word_index in range(len(words)):
            lps = self._compute_lps_array(words[current_word_index])
            # Compare the current word with all other words.
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index:
                    continue  # Skip comparing the word with itself.

                # Check if the current word is a substring of another word.
                if self._is_substring_of(
                    words[current_word_index], words[other_word_index], lps
                ):
                    matching_words.append(words[current_word_index])
                    break  # No need to check further for this word.

        return matching_words

    # Function to compute the LPS (Longest Prefix Suffix) array for the substring 'sub'.
    def _compute_lps_array(self, sub: str) -> List[int]:
        lps = [0] * len(sub)
        current_index = 1
        length = 0

        while current_index < len(sub):
            if sub[current_index] == sub[length]:
                length += 1
                lps[current_index] = length
                current_index += 1
            else:
                if length > 0:
                    length = lps[
                        length - 1
                    ]  # Backtrack using LPS array to find a shorter match.
                else:
                    current_index += 1
        return lps

    # Function to check if 'sub' is a substring of 'main' using the KMP algorithm.
    def _is_substring_of(self, sub: str, main: str, lps) -> bool:
        main_index = 0
        sub_index = 0

        while main_index < len(main):
            if main[main_index] == sub[sub_index]:
                main_index += 1
                sub_index += 1
                if sub_index == len(sub):
                    return True  # Found a match.
            else:
                if sub_index > 0:
                    # Use the LPS to skip unnecessary comparisons.
                    sub_index = lps[sub_index - 1]
                else:
                    main_index += 1
        return False  # No match found.