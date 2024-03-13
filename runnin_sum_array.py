
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6


def number_5(next_list_5: list[int])-> list[int]: # this is my solution
    """the comments"""
    new_input = next_list_5
    result = []
    i = 0
    for num in new_input:
        i += num
        result.append(i)
    return result




# class Solution: this is karl's solution
#     def runningSum(self, nums: list[int]) -> list[int]:
#         # nums = [1, 2, 3, 4]
#         total = []
#         # for num in nums:
#         #     num +=
#         _sum = 0
#         for i in range(len(nums)):
#             total[i] = nums[i] + _sum
#             _sum = total[i]