class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left_index = 0
        right_index = len(numbers) - 1
        for i in range(len(numbers)):
            left_index = i
            while numbers[left_index] + numbers[right_index] > target:
                right_index -= 1 
            if numbers[left_index] + numbers[right_index] == target:
                return [left_index + 1, right_index + 1]
        return [left_index + 1, right_index + 1]