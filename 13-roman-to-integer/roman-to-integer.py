class Solution:
    def romanToInt(self, s: str) -> int:

        roman_dict={"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total=0

        prev_val=0

        for char in s:

            curr_value = roman_dict[char]

            total += curr_value

            if curr_value > prev_val:

                total -=2*prev_val

            prev_val = curr_value

        return total
        