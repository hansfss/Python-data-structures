#binary search for rotated lists (rotating implies removing the last element and adding it as the first element) - discover how many times each list has been rotated
#position of smallest number determines how many times the list has been rotated, this is the only number that is smaller than the number before it and smaller than the last number in the list
def first_instance(nums, pos, end):
    if nums[pos] <= nums[pos - 1] and nums[pos] <= nums[end]:
        if nums[pos - 1] == nums[pos] and end > 1: # end > 1 in case size of list is only 1
            return 'left'
        else:
            return 'found'
    else:
        if nums[pos] < nums[end]:
            return 'left'
        elif nums[pos] > nums[end]:
            return 'right'

def count_rotations_binary(nums):
    start, end = 0, len(nums) - 1

    while end >= start:
        pos = (start + end) // 2
        #print(pos)
        result = first_instance(nums, pos, end)

        if result == 'found':
            return pos
        elif result == 'left':
            end = pos - 1
        elif result == 'right':
            start = pos + 1
    return -1

test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}
test1 = {
    'input': {
        'nums': [13, 18, 29, 30, 36, 2, 3, 6]
    },
    'output': 5
}
test2 = {
    'input': {
        'nums': [13, 15, 17, 20, 21, 24, 28]
    },
    'output': 0
}
test3 = {
    'input': {
        'nums': [13, 1, 2, 3, 6, 9, 10, 12]
    },
    'output': 1
}
test4 = {
    'input': {
        'nums': [5, 8, 10, 14, 3]
    },
    'output': 4
}
test5 = {
    'input': {
        'nums': [3, 5, 8, 10, 14]
    },
    'output': 0
}
test6 = {
    'input': {
        'nums': []
    },
    'output': -1
}
test7 = {
    'input': {
        'nums': [420]
    },
    'output': 0
}
test8 ={
    'input': {
        'nums': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    },
    'output': 6
}
test9 = {
    'input': {         
        'nums': [5, 5, 6, 6, 6, 9, 9, 9, 9, 9, 11, 13, 16, 16, 16, 16, 16, 0, 0, 0, 0, 0, 0, 2]
    },
    'output': 17
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8, test9]

for i in range(0, len(tests)):
    result = count_rotations_binary(tests[i]['input']['nums'])
    ex_result = tests[i]['output']
    if result == ex_result:
        print('Success')
    else:
        print('Failed')

# def count_rotations_binary(nums):
#     start, end = 0, len(nums) - 1

#     while end >= start:
#         pos = (start + end) // 2

#         if nums[pos] <= nums[pos - 1] and nums[pos] <= nums[end]:
#             return pos
#         elif nums[pos] < nums[end]:
#             end = pos - 1
#         elif nums[pos] > nums[end]:
#             start = pos + 1
#     return -1