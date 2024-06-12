# This problem has a math trick that involves calculating
# all the numbers multiplied in order, from the start
# and all the numbers multiplied in order, backwards from the end
# Why?
# if you know this, you can pinpoint any part of the array
# and you can multiply the before (prefix) by the after (posfix)
# to get the multiple without using division
# [1, 2, 3, 4]
# For example, you want 1 x 2 x 4 for the 3 slot
# So you figure out what 1 x 2 is (prefix)
# And you multiply that by 4 x 1 (postfix)
# Even worse, you store them in an answer array so you don't take up any more space

# Remember: The answer array is storing the products of all elements BEFORE the current index. Not at the current index; you got confused about this


class Solution:
    def productArray(self, nums):

        answer = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, - 1, - 1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


class Brute:
    def productArray(self, nums):
        if len(nums) < 3:
            return None

        answer = []

        for number in nums:
            product_nums = [*nums]
            product_nums.remove(number)

            product = 1
            for number in product_nums:
                product *= number
            answer.append(product)

        return answer


solution = Solution()
print(solution.productArray([1, 2, 3, 4]))
