class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        resp = 0
        index = 0
        for element in s:

            current = roman_values[element]

            if index + 1 == len(s):
                resp = resp + current

            elif element == 'C' and (s[index+1] == 'M' or  s[index+1] == 'D'):
                resp = resp - 100

            elif element == 'X' and (s[index+1] == 'L' or  s[index+1] == 'C'):
                resp = resp - 10

            elif element == 'I' and (s[index+1] == 'V' or  s[index+1] == 'X'):
                resp = resp - 1

            else:
                resp = resp + current

            index += 1

        return resp