"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""

"""my solution
使用一个栈，如果是前半部分就进栈，如果是后半部分就出栈 ，并测试是否匹配
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        push_list = ['(','[','{']
        pop_list = [')',']','}']
        for single_char in s:
            if single_char in push_list:
                stack.append(single_char)
            if single_char in pop_list:
                if single_char == ')':
                    if len(stack)==0 or stack.pop() != '(':
                        return False
                elif single_char ==']':
                    if len(stack)==0 or stack.pop() != '[':
                        return False
                elif single_char == '}':
                    if len(stack)==0 or stack.pop() != '{':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False

"""前面我定义了两个list，其实可以定义成一个dict 最后的判断stack是否为空也可以写成一条语句"""
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []