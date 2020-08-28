"""
20. Valid Parentheses
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
Runtime: 12 ms, faster than 98.73% of Python online submissions for Valid Parentheses.
Memory Usage: 12.7 MB, less than 98.26% of Python online submissions for Valid Parentheses.
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

        if s == "":
            return True
        else:
            for key in pair:
                if key not in s:    # Return False, if any 'closing' parentheses exists, even though there is no 'opening' pair-parentheses.
                    if s.count(pair[key]) != 0:
                        return False
                else:    # For every 'opening' parentheses in input 's', check if i+1, i+3, i+5, ..-th elements are their 'pair' parentheses (here i: index of 'opening' parentheses).
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

        # Less filtering conditions are written here.
        if 0 not in checkpair:
            return True
        else:
            return False

s = "()[]{}"
ValPar = Solution()
print(ValPar.isValid(s))

"""
This code can filter the input from the beginning.
Simple filtering conditions are moved to the front for even efficient computation.
As a result, unnecessary further computation can be avoided.
"""