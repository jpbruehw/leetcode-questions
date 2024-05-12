# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# brute force solution
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(set(s)) == 1: return 1
    res = 0
    
    for l in range(len(s)):
        temp = set()
        temp.add(s[l])
        r = l + 1
        while r < len(s) and s[r] not in temp:
            temp.add(s[r])
            res = max(res, len(temp))
            r += 1
    return res

# good solution
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(set(s)) == 1: return 1

    char_set = set()
    l, res = 0, 0
    
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r-l+1)
    return res