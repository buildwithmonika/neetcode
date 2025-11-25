# ======== PROBLEM =======
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true
# ======== PROBLEM END =======

# first solution

# lst = [1, 2, 3, 3]
# dicts = {}
# duplicate_found = False
# for x in lst:
#     if dicts.get(x):
#         duplicate_found = True
#         print(True)
#         break
    
#     dicts[x] =  1

# if not duplicate_found:
#     print(False)

# pythonic

lst = [1,1,1,3,3,4,3,2,4,2]

# if len(lst) == len(set(lst)):
#     print(False)
# else:
#     print(True)


#submitted solution
def has_duplicate(nums):
    return len(nums) != len(set(nums))

has_duplicate(lst)