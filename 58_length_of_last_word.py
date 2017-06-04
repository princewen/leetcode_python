"""

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length = length + 1
            else:
                break

        return length

"""other solution"""
def lengthOfLastWord(self, s):
    return len(s.rstrip(' ').split(' ')[-1])
