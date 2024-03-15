
# https://leetcode.com/problems/concatenation-of-array/description/
nums = [1, 2, 3]

f_nums = nums
n_nums = f_nums.copy()
ans = f_nums + n_nums
print(ans)

# basically, returning the  input list twice, I used copy() in order to use + and add them together