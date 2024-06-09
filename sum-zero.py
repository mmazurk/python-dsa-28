class SumZero(object):
    def sumZero(self, arr):
        if len(arr) == 0:
            return None

        left_index = 0
        right_index = len(arr) - 1

        while left_index < right_index:
            sum = arr[left_index] + arr[right_index]
            if sum == 0:
                return [arr[left_index], arr[right_index]]
            elif sum > 0:
                right_index -= 1
            else:
                left_index += 1

        return None


solution = SumZero()
print(solution.sumZero([-3, -2, -1, 0, 1, 2, 3]))
print(solution.sumZero([-11, -9, -1, 0, 1, 2, 3]))
print(solution.sumZero([-2, 0, 1, 3]))
print(solution.sumZero([1, 2, 3]))
