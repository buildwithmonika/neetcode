# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

#submitted solution

from collections import Counter
strs = ["act","pots","tops","cat","stop","hat"]
seen = {}
lst = []

for x in strs:
    counter = "".join(sorted(x))
    if counter in seen:
        seen[counter].append(x)
    else:
        seen[counter] = [x]

print(list(seen.values()))

        

        