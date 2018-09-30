'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

'''

def maxArea(self, height):
    width = len(height) - 1
    left = 0
    right = len(height) - 1
    result = 0

    for w in range(width, 0, -1):
        if height[left] < height[right]:
            result = max(result, height[left] * w)
            left += 1
        else:
            result = max(result, height[right] * w)
            right -= 1

    return result