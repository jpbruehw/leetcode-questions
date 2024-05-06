# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# solution 1:
def majorityElement(nums: List[int]) -> int:
    counter = {}
    for num in nums:
        if num in counter.keys():
            counter[num] += 1
        else:
            counter[num] = 1
    
    return max(counter, key=counter.get)

# solution 2:
def majorityElement(nums: List[int]) -> int:
    res = None
    count = 0
    for n in nums:
        if count == 0:
            res = n
        count += 1 if n == res else -1

    return res
