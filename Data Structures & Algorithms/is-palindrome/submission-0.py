class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""
        for c in s:
            if c.isalnum():#checks if alphanumeric or not
                newstr+=c.lower()
        return newstr==newstr[::-1]