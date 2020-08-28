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
Runtime: 2660 ms, faster than 6.29% of Python online submissions for Valid Parentheses.
Memory Usage: 13 MB, less than 17.66% of Python online submissions for Valid Parentheses.
"""

class Solution (object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pair = {"(":")", "{":"}", "[":"]", ")":"", "}":"", "]":""}

        i = -1
        checkpair = []
        while i <= len(s)-2:
            i += 1
            j = 1
            k = 0

            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                while i + j <= len(s) - 1:
                    if pair[s[i]] == s[i + j]:
                        k += 1
                        j += 2

                    else:
                        j += 2
                checkpair.append(k)

        del checkpair[len(checkpair)-1]
        print(checkpair)

        if 0 not in checkpair and len(checkpair)!=0 and s.count('(')==s.count(')') and s.count('[')==s.count(']') and s.count('{')==s.count('}') or s == "":
            return True
        else:
            return False

s = "()[]{}"
ValPar = Solution()
print(ValPar.isValid(s))