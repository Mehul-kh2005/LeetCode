class Solution:
    def romanToInt(self, s: str) -> int:
        
        # create a hashmap for our values
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        # create a result value to be returned
        result = 0
        
        for i in range(len(s)):
            # check if there is a "next value" (i + 1)
            # if there is then check if the next value is greater than the previous
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                # if the previous value is less, we subtract that value from the result
                result -= roman[s[i]]
            # otherwise we add it to our result
            else: 
                result += roman[s[i]]
            # we return the result we find
        return result