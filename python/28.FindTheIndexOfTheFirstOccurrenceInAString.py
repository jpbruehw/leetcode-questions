# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def strStr(self, haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0
    n = len(haystack)
    n_2 = len(needle)
    for i in range(n):
        if haystack[i:i+n_2] == needle:
            return i
    
    return -1