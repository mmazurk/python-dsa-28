class Solution:
    def bestTimeToSell(self, prices):
        """Leetcode"""

        left_index = 0
        right_index = 1
        profit = 0

        while right_index < len(prices):
            if prices[right_index] < prices[left_index]:
                left_index = right_index
                right_index += 1
            else:
                profit = max(profit, prices[right_index] - prices[left_index])
                right_index += 1

        return profit

# I did a great job solving this
# But the problem was that I thought it was sliding window when actually it was two pointer


solution = Solution()
print(solution.bestTimeToSell([2, 1, 2, 1, 0, 2]))
print(solution.bestTimeToSell([]))
print(solution.bestTimeToSell([]))
print(solution.bestTimeToSell([]))
print(solution.bestTimeToSell([]))
