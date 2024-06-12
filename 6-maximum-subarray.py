class Solution:
    """Leetcode hell"""

# This is dynamic programming using tabulation
# Tabluation is usually iteration and memoization involves recursion (to prevent expensive caluclation)
# This has optimal substructure and overlapping subproblems

# This was really hard for me to wrap my brain around because it's new
# This method keeps track of two things:
# A global sum and current sum
# If the current sum goes below zero (e.g., we've had a series of negative numbers)
# It resets to zero and starts over again
# This is called Kadane's Algorithm (shit, it has a name)

    def maxSubArray(self, nums):
        """Leetcode"""

        global_sum = nums[0]
        current_sum = 0

        for number in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += number
            global_sum = max(global_sum, current_sum)

        return global_sum


solution = Solution()
print(solution.maxSubArray([-1, -2, -3, -4]))
