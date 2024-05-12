# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

# brute force solution
# too slow and not linear time
def maxArea(self, height: List[int]) -> int:
       res = 0

       for l in range(len(height)):
           for r in range(l + 1, len(height)):
               # width (r-l) * height (min(height[r], height[l]))
               area = (r - l) * min(height[r], height[l])
               res = max(res, area)
       return res

# optimal solution
def maxArea(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    res = 0
    
    while l < r:
        area = (r - l) * min(height[r], height[l])
        res = max(res, area)
        
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        # could eliminate this line
        else:
            r -= 1
    return res