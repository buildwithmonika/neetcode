# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]


# first solution 
# from collections import Counter
nums = [3,3,1,1,1,2,3,3, 4,4,4]
k = 2
# output_lst = []

# count_freq = Counter(nums)
# sorted_freqs = dict(sorted(count_freq.items(), key=lambda item: item[1], reverse=True))

# for key, v in sorted_freqs.items():
#     if len(output_lst) == k:
#         break
#     else:
#         output_lst.append(key)

# print(output_lst)
# print(len(nums))

# submitted solution
count = {}
freq = [[] for i in range(len(nums) + 1)]

for num in nums:
    count[num] = 1 + count.get(num, 0)
for num, cnt in count.items():
    freq[cnt].append(num)

res = []
for i in range(len(freq) - 1, 0, -1):
    for num in freq[i]:
        if len(res) != k:
            res.append(num)

print(res)
