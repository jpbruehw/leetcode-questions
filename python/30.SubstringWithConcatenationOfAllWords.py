# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

# solution vid: https://www.youtube.com/watch?v=-wlDdMmaYwI&t=1s

def findSubstring(self, s: str, words: List[str]) -> List[int]:
    # base case if blanks are passed in
    if not s or not words:
        return []
    
    # create a hashmap to store the frequncy of words
    # we use this to check against the occurances in the
    # string, the instances have to match the frequency
    # here otherwise the starting index is invalid
    word_freq = {}
    for word in words:
        # either assign one or update one if it is
        # already in the map
        word_freq[word] = 1 + word_freq.get(word, 0)
    
    # we know from the question each word is the same length
    # therefore, the window size is simply the length of the
    # words times the number of words
    word_len = len(words[0])
    window_len = len(words) * word_len
    res = []
    # iterate through the string
    # we add 1 to the delta between len and the window len
    # to ensure the last starting index is included
    for i in range(len(s) - window_len + 1):
        # create a temporary hash map
        # that will store the frequencies in the window
        substr_freq = {}
        # we start j at i and then increment
        # j by the length of a single word until
        # it reaches the end of window
        j = i
        while j < i + window_len:
            # get the current word, since the length
            # will always be the same no matter what
            cur_word = s[j:j+word_len]
            # if the word is not in the map we created
            # then we can break the loop since we know the
            # condition will not be fulfilled
            if cur_word not in word_freq:
                break
            # if the word is present, update the temporary hashhmap
            # we will then check that this matches with the frequency
            # in the reference hash map
            substr_freq[cur_word] = substr_freq.get(cur_word, 0) + 1
            # if the word appears more in the window than the reference
            # we can break the loop since the frequency is greater than what
            # we would expect
            if substr_freq[cur_word] > word_freq[cur_word]:
                break
            j += word_len
        # if j reaches the end of the end of the window
        # its value will be equal to the starting position
        # of the next window and if this is true,
        # we add the i to the res since we know it is a valid starting
        # position
        if j == i + window_len:
            res.append(i)
    
    return res