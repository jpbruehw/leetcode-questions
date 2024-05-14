# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# video solution: https://www.youtube.com/watch?v=TjFXEUCMqI8

def isValidSudoku(self, board):
    # res list to store the values
    # what we need to essentially check is that
    # there are no duplicate values at all and
    # in order to do that we need to create a tuple
    # that contains the coordinates [i,j] and the value
    # if the board is valid, each value at i and j will
    # be unique, then we also need a way to check the matrix that
    # the value is in, we know that the matrix is 3x3
    # so we can use floor division to essentially represent which
    # of the nine matrices the given value is in
    # by floor dividing by three, we can use the remainders
    # to represent the coordinates of the matrix
    res = []
    # we know the length of each list
    # is 9 so we can hardcode it
    # we use a nested loop to essentially
    # get the coordinates from the matrix
    # the i represents the row and the j
    # represents the column
    for i in range(9):
        for j in range(9):
            # get the element based on the coordinates
            # if it is a ., we can ignore it since we only
            # need to check if the number is valid
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    # finally, we check that the length of the res list is the same as the set
    # version of this, if the lengths don't match, we know there was a duplicate
    # and we can't have that
    return len(res) == len(set(res))