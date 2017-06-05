"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
"""
两个指针，用isalnum判断是否是字母，注意统一转换成小写然后再比较
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        else:
            i = 0
            j = len(s) - 1
            while i < j:
                while i < j and not s[i].isalnum():
                    i = i + 1
                while i < j and not s[j].isalnum():
                    j = j - 1
                if s[i].lower() != s[j].lower():
                    return False
                i = i + 1
                j = j - 1
            return True
