"""
Problem Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.



Submission result:
Runtime: 20 ms, faster than 88.10% of Python online submissions for Longest Common Prefix.
Memory Usage: 12.7 MB, less than 80.83% of Python online submissions for Longest Common Prefix.
"""

class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: list[str]
        :rtype: str
        """

        i = 0
        common = ''
        prefix = ''
        noprefix = ''

        if strs == []:  # if input is an empty list, return an empty string.
            return noprefix

        else:

            shortchar = min(strs, key=len)  # find the shortest string in the list
            shortlen = len(shortchar)   # length of the shortest string

            while i < shortlen:
                for str in strs:
                    common += str[i]

                if common == len(strs) * shortchar[i]:  # check if 'i'th letter of the elements are matched
                    prefix += shortchar[i]  # if match, add the common letter to a variable 'prefix'
                else:
                    prefix += 'A'   # if do not match, add 'A' to a variable 'prefix'. A capital letter 'A' is randomly chosen to distinguish it from the common letters, which are lowercase letters.

                i += 1
                common = '' # reset variable 'common'

            if shortchar == '':
                return noprefix # if the shortest string is '', return an empty string.
            elif prefix[0] != shortchar[0]:
                return noprefix # if the first letter is not a common letter, which means there is no prefix, return an empty string.
            else:
                prefix = prefix.replace('A', '')
                # print(prefix)   # 값을 return 하기 전에는 출력 . 정확한 이유는 알아볼 것.
                return prefix   # otherwise, remove the capital 'A's, and return only the common prefix
                # print(prefix)   # 값을 return 한 이후에는 출력 안됨. 정확한 이유는 알아볼 것.



strs = ["flower", "flow", "flight"]
prefix = Solution()
prefix.longestCommonPrefix(strs)

# 실행 결과를 출력 해보고 싶을 때:
# ans = prefix.longestCommonPrefix(strs)
# print(ans)