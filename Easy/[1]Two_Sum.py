"""
1. Two Sum
Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Submission result:
Runtime: 32 ms, faster than 96.62% of Python online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 27.85% of Python online submissions for Two Sum.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dic = {}

        for index in range(len(nums)):
            if not (target - nums[index]) in num_dic:
                num_dic[nums[index]] = index
            else:
                return index, num_dic[target - nums[index]]