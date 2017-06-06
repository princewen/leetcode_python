"""

Write a function to find the longest common prefix string amongst an array of strings.

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        cpre = strs[0]
        for onestr in strs[1:]:
            i = 0
            while i < len(cpre) and i < len(onestr) and cpre[i] == onestr[i]:
                i = i + 1
            cpre = cpre[:i]

        return cpre


"""an answer using zip"""


def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ''
    l = 0
    for cg in zip(*strs):
        if len(set(cg)) > 1:
            return strs[0][:l]
        l += 1
    return strs[0][:l]