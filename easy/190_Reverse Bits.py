"""

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

"""

"""
my solution

"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        stack = []
        while n:
            stack.append(n%2)
            n /= 2
        while(len(stack)<32):
            stack.append(0)
        for i in range(0,len(stack)):
            n = n*2+stack[i]
        return n