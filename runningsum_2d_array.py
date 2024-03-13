
# Richest Customer Wealth

# https://leetcode.com/problems/richest-customer-wealth/description/

bank_accounts = [[1, 8, 3], [1, 2, 3]]
w = 0
riches = []
for i in bank_accounts:
    wealth = sum(i)
    riches.append(wealth)

print(riches)
print(max(riches))


