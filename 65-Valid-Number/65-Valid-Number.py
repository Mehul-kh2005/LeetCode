class Solution:
    def isNumber(self, s: str) -> bool:
        # Check if the input string is empty
        if not s:
            return False
        
        i = 0

        # Handle optional sign at the beginning
        if s[i] in ['+', '-']:
            i += 1
        
        # Flags to track the presence of a decimal point and digits
        decimal_seen = False
        number_seen = False

        # Process each character in the string
        while i < len(s):
            c = s[i]

            # Handle decimal point
            if c == '.':
                if decimal_seen:
                    return False  # More than one decimal point is invalid
                decimal_seen = True
            
            # Handle exponent part
            elif c in ['e', 'E']:
                # Exponent should be preceded by a number
                if not number_seen:
                    return False
                # Check if exponent part is a valid number
                return self.is_valid_number(s[i+1:])
            
            # Handle invalid sign character or letter
            elif c in ['+', '-']:
                return False
            
            # Handle digit characters
            elif c.isdigit():
                number_seen = True
            
            # Handle any other character
            else:
                return False
            
            i += 1
        
        # Check if at least one number was seen
        return number_seen

    def is_valid_number(self, num_string: str) -> bool:
        # If the exponent part is empty, it is invalid
        if not num_string:
            return False

        i = 0

        # Handle optional sign in the exponent part
        if num_string[i] in ['+', '-']:
            i += 1
        
        # Flag to ensure there's at least one digit in the exponent part
        number_seen = False

        # Process each character in the exponent part
        while i < len(num_string):
            c = num_string[i]
            
            # Exponent part must only contain digits
            if not c.isdigit():
                return False
            number_seen = True

            i += 1

        # Ensure that there is at least one digit in the exponent part
        return number_seen