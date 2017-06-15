"""

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5


"""

"""要考虑连续空格的情形"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ss = s.split(' ')
        return len([x for x in ss if x.strip() != ''])

"""其实一行就可以完成！不指定分隔符默认按照空格进行划分，包括连续的空格！"""
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


