
# https://leetcode.com/problems/two-sum/

def twosum(nums: list[int], target: int) -> list[int]:
    """return the indices of the two numbers such that they up to the target."""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == total:
                return [i, j]


input_list = [8, 2, 7, 8]
total = 9

d = twosum(input_list, total)
print(d)

# using  "i+1" inside the second loop allows me to work with index[1] , since I already got the index[0] in
# the previous loop.
