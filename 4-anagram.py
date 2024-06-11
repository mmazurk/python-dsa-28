class Solution:
    def isAnagram(self, t, s):
        """Leetcode"""

        if len(t) != len(s) or len(t) == 0:
            return None

        def hashLetters(string):
            hash_table = {}
            for letter in string:
                hash_table[letter] = hash_table.get(letter, 0) + 1

            return hash_table

        hashed_t = hashLetters(t)
        hashed_s = hashLetters(s)

        return hashed_t == hashed_s


solution = Solution()
print(solution.isAnagram("mark", "kram"))
