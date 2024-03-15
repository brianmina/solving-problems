
# https://leetcode.com/problems/running-sum-of-1d-array/description/

def number_5(next_list_5: list[int])-> list[int]: # this is my solution
    """the comments"""
    new_input = next_list_5
    result = []
    i = 0
    for num in new_input:
        i += num
        result.append(i)
    return result

# I used the  += operation so that I can add a sum in every loop.


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