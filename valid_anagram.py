# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# mine

# s_hash = {}
# t_hash = {}

s = "racecar"
t = "carracd"

# for x in s:
#     if x in s_hash:
#         s_hash[x] = s_hash.get(x) + 1
#     else:
#         s_hash[x] = 1

# for x in t:
#     if x in t_hash:
#         t_hash[x] = t_hash.get(x) + 1
#     else:
#         t_hash[x] = 1

# is_valid = False
# if len(s_hash.keys()) == len(t_hash.keys()):
#     is_valid = True
#     for x in s_hash:
#         if x not in t_hash or t_hash.get(x) != s_hash.get(x):
#             is_valid = False
#             break
    
    
# if is_valid:
#     print("Valid dia")   
# else:
#     print("Invalid anagram.")            


# pythonic
from collections import Counter
print(Counter(s) == Counter(t))
 