"""

We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

"""

"""先统计，然后注意条件是exactly 1"""

import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict(collections.Counter(nums))
        max = 0
        for i in dic:
            if dic.get(i, 0) > 0 and dic.get(i + 1, 0) > 0 and dic.get(i, 0) + dic.get(i + 1, 0) > max:
                max = dic.get(i, 0) + dic.get(i + 1, 0)
        return max

"""同样的思路"""
def findLHS(self, A):
    count = collections.Counter(A)
    ans = 0
    for x in count:
        if x+1 in count:
            ans = max(ans, count[x] + count[x+1])
    return ans
