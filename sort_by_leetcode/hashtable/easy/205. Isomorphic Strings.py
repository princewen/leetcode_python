"""

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

"""

"""一开始我的解法是这样的，但是这是不对的，如下面的情况s='ab',t='aa' 就会出现错误"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = dict()
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            else:
                dic[s[i]] = t[i]
        return True
"""所以用两个dict分别对应保存两个字符串对应位置的对方字符，只要其中一个不满足条件，则返回错误"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic1 = dict()
        dic2 = dict()
        for i in range(len(s)):
            if (s[i] in dic1 and dic1[s[i]] != t[i]) or (t[i] in dic2 and dic2[t[i]] != s[i]):
                return False
            else:
                dic1[s[i]] = t[i]
                dic2[t[i]] = s[i]
        return True

"""其实，还有更简单的解法,使用zip将两个数组对应位置元素相连，再利用set不能有重复元素的特性，判断三者的长度是否相同即可"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))