"""

Total Accepted: 25680
Total Submissions: 44681
Difficulty: Easy
Contributors:
love_Fawn
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

"""

"""
my solution : 用数组保存下一个比他大的数

"""


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        dic = dict()
        max = nums[-1]
        dic[nums[-1]] = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max:
                dic[nums[i]] = -1
                max = nums[i]
            else:
                t = nums[i + 1]
                while (t != -1):
                    if t > nums[i]:
                        dic[nums[i]] = t
                        break
                    else:
                        t = dic[t]
                if t == -1:
                    dic[nums[i]] = -1

        return [dic[x] for x in findNums]

"""
https://discuss.leetcode.com/topic/77916/java-10-lines-linear-time-complexity-o-n-with-explanation
Suppose we have a decreasing sequence followed by a greater number. For example [5, 4, 3, 2, 1, 6] then the greater number 6 is the next greater element for all previous numbers in the sequence.
We use a stack to keep a decreasing sub-sequence, whenever we see a number x greater than stack.peek() we pop all elements less than x and for all the popped ones, their next greater element is x.
For example [9, 8, 7, 3, 2, 1, 6]. The stack will first contain [9, 8, 7, 3, 2, 1] and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6.
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        cache, st = {}, []
        for x in nums:
            if len(st) == 0:
                st.append(x)
            elif x <= st[-1]:
                st.append(x)
            else:
                while st and st[-1] < x:
                    cache[st.pop()] = x
                st.append(x)
        result = []
        for x in findNums:
            if x in cache:
                result.append(cache[x])
            else:
                result.append(-1)
        return result