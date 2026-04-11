class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1
        while left_index < right_index:
            current_sum = numbers[left_index] + numbers[right_index]

            if current_sum > target:
                right_index -= 1
            elif current_sum < target:
                left_index += 1
            else:
                return [left_index + 1, right_index + 1]
        return []