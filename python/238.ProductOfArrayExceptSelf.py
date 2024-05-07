# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def productExceptSelf(nums):
    n = len(nums)
    p = [1] * n
    s = [1] * n
    print("n_1", n)
    print("p_1", p)
    print("s_1", s)
    for i in range(1, n):
        p[i] = p[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        s[i] = s[i + 1] * nums[i + 1]
    print("n_2", n)
    print("p_2", p)
    print("s_2", s)
    a = [p[i] * s[i] for i in range(n)]
    return a