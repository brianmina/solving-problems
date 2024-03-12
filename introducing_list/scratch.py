

def running_sum(nums: list[int]) -> list[int]:
    run_nums = nums
    result = []
    i = 0
    for num in run_nums:
        i += num
        result.append(i)
    return result

numeros = [1, 1, 1, 1, 1, 1, 1, 1]

print(running_sum(numeros))

# def ()-> :
#     return
# print()


def number_2(run_list: list[int])->list[int]:
    """this function is going to do a running sum from a list of int"""
    user_input = run_list
    results = []
    i = 0
    for num in user_input:
        i += num
        results.append(i)
    return results


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number_2(new_list))


def number_3(run_nums: list[int])-> list[int]:
    """ next try"""
    user_input = run_nums
    result = []
    i = 0
    for num in user_input:
        i += num
        result.append(i)
    return result


next_list = [5, 5, 5, 5, 5, 5]
print(number_3(next_list))


def number_4(list_input: list[int])-> list[int]:
    """ this function return a list of a running sum"""
    user_input = list_input
    result_list = []
    i = 0
    for num in user_input:
        i += num
        result_list.append(i)
    return result_list


example_4 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
print(number_4(example_4))


def number_5(next_list_5: list[int])-> list[int]:
    """the comments"""
    new_input = next_list_5
    result = []
    i = 0
    for num in new_input:
        i += num
        result.append(i)
    return result


example_5 = [1,2,3,4,5,6,7,8,9]
print(number_5(example_5))


bank_accounts = [[1,8,3], [1,2,3]]

w = 0
riches = []
for i in bank_accounts:
    wealth = sum(i)
    result = wealth
    riches.append(wealth)
    print(wealth)

print(max(riches))


