"""

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

"""

"""

利用十进制转二进制的方法，考虑十进制13
13 ／ 2 = 6 ----1
6 ／2 = 3 ----0
3 ／2 = 1 ----1
1 ／2 = 0 ----1
二进制是1101，前面补全0，而反转的二进制是1011，后面补全0
所以我们只需要按照除的顺序依次进入数组，后面不组32位用0补齐即可。

"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        stack = []
        while n:
            stack.append(n % 2)
            n = n / 2
        while len(stack) < 32:
            stack.append(0)
        ret = 0
        for num in stack:
            ret = ret * 2 + num
        return ret

