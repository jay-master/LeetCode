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

        # Create dictionary: pairs of parentheses
        pair = {"(": ")", "{": "}", "[": "]"}

        checkpair = []  # List to check improper pair

        for key in pair:
            if key in s:    # For every 'opening' parentheses in input 's', check if i+1, i+3, i+5, ..-th elements are their 'pair' parentheses (here i: index of 'opening' parentheses).
                if s.count(key) == s.count(pair[key]):  # Put a filtering condition at front part, instead back part. If input doesn't meet condition, the result returned immediately.
                    i = 1
                    j = 0   # Reset for the next element
                    while i + s.index(key) < len(s):
                        if s[s.index(key) + i] == pair[key]:
                            j += 1  # Increase variable 'j', if there are 'pair' of i-th element in i+1, i+3, i+5, ..-th position.
                            i += 2
                        else:   # Do not increase variable 'j', if there is no 'pair' of i-th element in i+1, i+3, i+5, ..-th position.
                            i += 2
                    checkpair.append(j) # After check i-th element (and i+1, i+3, i+5, ..-th elements), put variable 'j' in the list. If 'j' is 0, i-th element has no 'pair' in proper positions.
                else:
                    return False    # If input doesn't meet condition, the result returned immediately.
            else:
                if s.count(pair[key]) != 0:
                    return False    # Return False, if any 'closing' parentheses exists, even though there is no 'opening' pair-parentheses.

        print(checkpair)

        # Less filtering conditions are written here.
        if 0 not in checkpair and checkpair != [] or s == "":
            return True
        else:
            return False

s = "()[]{}"
ValPar = Solution()
print(ValPar.isValid(s))

"""
This code can filter the input from the beginning.
As a result, unnecessary further computation can be avoided.
"""