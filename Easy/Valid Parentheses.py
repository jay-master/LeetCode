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

        # Create dictionary: pairs of parentheses
        # Last 3 pairs are added because of the error occurred during processing 'if' below.
        pair = {"(":")", "{":"}", "[":"]", ")":"", "}":"", "]":""}

        i = -1
        checkpair = []  # List to check improper pair

        while i <= len(s)-2:
            i += 1
            j = 1   # Reset for the next element
            k = 0   # Reset for the next element

            if s[i] == "(" or s[i] == "{" or s[i] == "[":   # Check every i-th elements which are 'opening' of parentheses, if i+1, i+3, i+5, ..-th elements are their 'pair' parentheses.
                while i + j <= len(s) - 1:
                    if pair[s[i]] == s[i + j]:
                        k += 1  # Increase variable k, if there are 'pair' of i-th element in i+1, i+3, i+5, ..-th position.
                        j += 2

                    else:   # Do not increase variable k, if there is no 'pair' of i-th element in i+1, i+3, i+5, ..-th position.
                        j += 2
                checkpair.append(k) # After check i-th element (and i+1, i+3, i+5, ..-th elements), put variable k in the list. If k is 0, i-th element have no 'pair' in proper position.

        del checkpair[len(checkpair)-1] # Delete the last element of the list. Put due to an wrong result occurred, when len(s)=2 (ex: "()"). Expected result is 'True' but returns 'False', as the list 'checkpair' is [1,0].
        print(checkpair)

        # Many filtering conditions are written here.
        if 0 not in checkpair and len(checkpair)!=0 and s.count('(')==s.count(')') and s.count('[')==s.count(']') and s.count('{')==s.count('}') or s == "":
            return True
        else:
            return False

s = "()[]{}"
ValPar = Solution()
print(ValPar.isValid(s))

"""
In the end this results in inefficient computation as the filtering is situated at the end, i.e., this code can not filter the input from the beginning.
If it can filter the input from the beginning, the rest of the computation is not required, i.e., more efficient.
"""