
#  Find the Pivot Integer

# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13

class Solution:
    def pivotInteger(self, n: int) -> int:
        y = n *(n + 1) // 2
        x = int(sqrt(y))
        if x * x == y:
            return x
        else:
            return -1

# I used the standar arimethic formula an then I took the square root   and compare if it is perfect or imperfect.