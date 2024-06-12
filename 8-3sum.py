
# The trick to this is that we are using a "home base" number
# And then we do left and right pointers from there
# We also sort the array to make things easier


class Solution:
    def threeSum(self, nums):
        """Leetcode Hell"""

        results = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    results.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return results


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, 4]))
