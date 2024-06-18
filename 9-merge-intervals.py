

# The way to solve this is to draw it out
# And then figure out a way to process all the edge cases
# A key factor in solving this problem is sorting it first
# Which automatically makes it O(n log n)

# I struggled because I didn't know how to use unpacking
# so I could track the start, end of each pair
# This also uses the strategy of putting the first element
# in the answer bucket and then comparing each with it


class Solution:
    def mergeIntervals(self, intervals):
        """Leetcode. What are you gonna do?"""

        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])

        return output


solution = Solution()
print(solution.mergeIntervals([[1, 5], [1, 10], [11, 12]]))
