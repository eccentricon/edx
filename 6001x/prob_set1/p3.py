# s = "azcbobobegghakl"
# s = "abcbcd"
s = "abcbcdawxyz"
expected = "beggh"
longest_ss = s[0]
temp_ss = ""

for i in range(len(s)):
    if i > 0 and s[i] >= temp_ss[-1]:
        temp_ss += s[i]  # append the letter
        if len(temp_ss) > len(longest_ss):
            # make temp the longest
            longest_ss = temp_ss[:]  # copy!
    else:  # start a new temp_ss
        temp_ss = s[i]

print("Longest substring in alphabetical order is:", longest_ss)