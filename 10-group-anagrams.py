# My solution is unfinished. I was on the right track counting the letters using a hash table
# But I couldn't figure out how to follow through on the idea and compare the hash tables
# then group them together

class MySolution():
    def groupAnagrams(self, strs):

        answer = []

        def countLetters(str):
            dict = {}
            for letter in str:
                dict[letter] = dict.get(letter, 0) + 1
            return dict

        for string in strs:
            answer.append(countLetters(string))

        return answer
        # [{'e': 1, 'a': 1, 't': 1}, {'t': 1, 'e': 1, 'a': 1}, {'t': 1, 'a': 1, 'n': 1}, {'a': 1, 't': 1, 'e': 1}, {'n': 1, 'a': 1, 't': 1}, {'b': 1, 'a': 1, 't': 1}]


class LeetSolution():
    def groupAnagrams(self, strs):

        # First set up a dict object to hold all your counts
        res = {}

        # Create an array with 26 zeros in it
        for s in strs:
            count = [0] * 26

            # for each of the 26 array slots with zeros, add 1 every time that letter is used
            for c in s:
                count[ord(c) - ord("a")] += 1

            # now make the list/array a key
            key = tuple(count)

            # make the key if necessary and if it exists, append the word
            # pay attention here; you are initializing the value to be array and appending to the array
            if key not in res:
                res[key] = []
            res[key].append(s)

        # now just return the values, which are all arrays
        return res.values()


class AlternateSolution():
    def groupAnagrams(self, strs):

        counts = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in counts:
                counts[key] = []

            counts[key].append(s)

        return counts.values()


solution = AlternateSolution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
