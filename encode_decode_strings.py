# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode
# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

lst = ["4#neet", "code", "love", "you"]


def encode(strs):
    return ''.join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    result = []
    i = 0
   
    while i < len(s):
        j = s.find('#', i)
        length = int(s[i:j])
        start = j + 1
        end = start + length
        result.append(s[start:end])
        i = end

    return result

encoded_lst = encode(lst)

print(encoded_lst)
print(decode(encoded_lst))