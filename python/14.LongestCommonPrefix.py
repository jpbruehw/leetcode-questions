# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    
    r = ""
    shortest_tuple = min([(s, len(s)) for s in strs], key=lambda x: x[1])
    for i in range(shortest_tuple[1]):
        temp = 0
        char_check = shortest_tuple[0][i]
        for s in strs:
            if s[i] == char_check:
                temp += 1
        if temp == len(strs):
            r += char_check
        else:
            break
    return r
                