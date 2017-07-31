"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


"""
"""回溯法，类似于穷举"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.dfs('', [], 0, 0, n)

    def dfs(self, now_res, res, open, close, n):
        if len(now_res) == n * 2:
            res.append(now_res)
        if open < n:
            self.dfs(now_res + '(', res, open + 1, close, n)
        if close < open:
            self.dfs(now_res + ')', res, open, close + 1, n)
        return res


