# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water.

# This had to be either two-pointer or sliding window.

class Solution():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = min(height[left], height[right])*(right-left)

        while (left < right):
            if height[left + 1] > height[right - 1]:
                left = left + 1
            else:
                right = right - 1

            currentArea = min(height[left], height[right])*(right-left)
            area = max(area, (min(height[left], height[right])*(right-left)))

        return area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
