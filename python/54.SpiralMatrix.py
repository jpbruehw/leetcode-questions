# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# solution: https://www.youtube.com/watch?v=BJnMZNwUk1M

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    # we start left at zero naturally and then
    # the right is the length of the first list
    # this essentially tells us the number of columns
    left, right = 0, len(matrix[0])
    # the top is also initialized to 0 and
    # the bottom is the length of the matrix itself
    # this gives us the number of rows
    # we can't initialize bottom or right to len-1
    # since we are passing these values in to create
    # ranges sometimes and need the last value to be excluded 
    top, bottom = 0, len(matrix)
    # the breaking condition is essentially that any
    # of the pointers cross, when this happens
    # we know that we have reached the end of the spiral
    while left < right and top < bottom:
        # the first step is to get every value
        # in the top row
        # go from left to right since these values
        # will change as the loop continues
        for i in range(left, right):
            # now we return all the values in the
            # the current top row and once
            # the loop finishes we shift top down
            res.append(matrix[top][i])
        top += 1
        # now we need to get all the values in the
        # right most column and return those
        # to do this we need to go from top to bottom
        # we can do this because we just shifted the top
        # value down one row
        for i in range(top, bottom):
            # we can access the correct row using i
            # and then get all the last values in each
            # row using the right value, we subtract 1 to
            # account for the length to index
            res.append(matrix[i][right - 1])
        right -= 1
        # sometimes the condition is already satisfied in
        # before each iteration completes
        # in this case we need to terminate the loop early
        # otherwise the loop will keep going through and won't
        # terminate until a full iteration is complete
        # it can be that either top, or right already
        # the condition is only checked once at the beginning
        # each iteration which is why we need this check
        # after right and top are updated
        if not (left < right and top < bottom):
            break
        # now we need to account for the last row
        # and go right to left to get the final row
        # by passing in -1 to range we can create a reverse
        # list of indices essentially
        # we subtract 1 from left so the left most index is included
        for i in range(right - 1, left - 1, -1):
            # so iterate backwards through the bottom
            # row and then add those values to the list
            res.append(matrix[bottom - 1][i])
        # when complete we then need to subtract one
        # from the bottom value to shift it up
        bottom -= 1
        # finally, we iterate from bottom to the top
        # to get the values in the left most column
        # we subtract 1 from bottom and top as well
        # to get the range of values between them
        # and since we are going bottom to top we iterate backwards
        # to get the left most value in each column
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
    return res