class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # For every index, store the valid multiplier
        muls = []
        running_mul = 1

        # Stack to take care of nested formula
        stack = [1]

        # Preprocess the formula and extract all multipliers
        index = len(formula) - 1
        curr_number = ""
        while index >= 0:
            if formula[index].isdigit():
                curr_number += formula[index]

            # If we encountered a letter, then the scanned
            # number was count and not multiplier. Discard it.
            elif formula[index].isalpha():
                curr_number = ""

            # If we encounter a right parenthesis, then the
            # scanned number was a multiplier. Store it.
            elif formula[index] == ")":
                curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul *= curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ""

            # If we encounter a left parenthesis, then the
            # most recent multiplier will cease to exist.
            elif formula[index] == "(":
                running_mul //= stack.pop()
                curr_number = ""

            # For every index, store the valid multiplier
            muls.append(running_mul)
            index -= 1

        # Reverse the muls
        muls = muls[::-1]

        # Map to store the count of atoms
        final_map = defaultdict(int)

        # Traverse left to right in the formula
        index = 0
        while index < len(formula):
            # If UPPER CASE LETTER, extract the entire atom
            if formula[index].isupper():
                curr_atom = formula[index]
                curr_count = ""
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1

                # Extract the count
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1

                # Update the final map
                if curr_count:
                    final_map[curr_atom] += int(curr_count) * muls[index - 1]
                else:
                    final_map[curr_atom] += 1 * muls[index - 1]

            else:
                index += 1

        # Sort the final map
        final_map = dict(sorted(final_map.items()))

        # Generate the answer string
        ans = ""
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])

        return ans