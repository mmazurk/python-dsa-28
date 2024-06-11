class Solution1:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution1()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))

# This is a brute force approach and is O(N^2).
# Space complexity if O(1) because no extra space is used to do the calculation.
# If you want to make it O(N) then you can only iterate through the array once.
# What does that mean? It means you need to store those key-value pairs in a dictionary (hash table).
# That's exactly what I do in the solution below. The cost is space complexity of O(N).
# Don't forget you can do two separate (or three) separate loops through the array and still be O(N).


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numbers_dict = {}
        for i in range(len(nums)):
            numbers_dict[nums[i]] = i

        for i in range(len(nums)):
            looked_for = target - nums[i]
            if looked_for in numbers_dict and numbers_dict[looked_for] != i:
                return [i, numbers_dict[looked_for]]

# Note that in Python I don't use myObject.hasOwnProptery() to see if the object has as key
# Rather, I use "in" which will check for the key
# if looked_for in numbers_dict
# I could have done if looked_for in numbers_dict.keys() but this would iterate through the keys to build an object
# You would have to use this approach for if value in looked_for.values()


solution = Solution2()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
