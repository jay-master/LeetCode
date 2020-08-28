"""
Problem Description:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true



Submission Result:
Runtime: Runtime: 20 ms, faster than 81.04% of Python online submissions for Valid Parentheses.
Memory Usage: 12.9 MB, less than 30.01% of Python online submissions for Valid Parentheses.
"""

class Solution (object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pair = {"(": ")", "{": "}", "[": "]"}
        checkpair = []
        for key in pair:
            if key in s:
                if s.count(key) == s.count(pair[key]):
                    i = 1
                    j = 0
                    while s.index(key) + i < len(s):
                        if s[s.index(key)+i] == pair[key]:
                            j += 1
                            i += 2
                        else:
                            i += 2
                    checkpair.append(j)
                else:
                    return False
            else:
                if s.count(pair[key]) != 0:
                    return False

        print(checkpair)
        if 0 not in checkpair and checkpair != [] or s == "":
            return True
        else:
            return False

s = "[])"
ValPar = Solution()
print(ValPar.isValid(s))