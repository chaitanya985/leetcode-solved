class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_palindrome(left: int, right: int, skip: bool) -> bool:
           
            if left >= right:
           
                return True
           
            if s[left] == s[right]:
           
                return check_palindrome(left + 1, right - 1, skip)
           
            if skip:
           
                return False
           
            return check_palindrome(left + 1, right, True) or check_palindrome(left, right - 1, True)

        return check_palindrome(0, len(s) - 1, False)
        