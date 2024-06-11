
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution1:
    def containsDuplicate(self, nums):
        """Leetcode hell"""
        if (len(nums) <= 1):
            return False

        number_counts = {}
        for number in nums:
            number_counts[number] = number_counts.get(number, 0) + 1

        for number in number_counts.values():
            if number > 1:
                return True
        return False

# In this solution, we just add numbers to a set and check to see if they are already there
# It's also O(N) like my solution above but it's a little less code.


class Solution2:
    def containsDuplicate(self, nums):
        """Leetcode"""

        numbers_set = set()
        for number in nums:
            if number in numbers_set:
                return True
            numbers_set.add(number)
        return False


solution = Solution2()
print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(solution.containsDuplicate([1]))
print(solution.containsDuplicate([]))
