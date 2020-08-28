"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



Submission Result:
Runtime: 20 ms, faster than 83.06% of Python online submissions for Reverse Integer.
Memory Usage: 12.8 MB, less than 20.96% of Python online submissions for Reverse Integer.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        xab = abs(x)
        if x >= 0:
            re = int(str(xab)[::-1])
        else:
            re = -int(str(xab)[::-1])

        if -2 ** 31 <= re <= 2 ** 31 - 1:
            return re
        else:
            return 0