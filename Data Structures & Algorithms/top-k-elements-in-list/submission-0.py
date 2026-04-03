class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}

        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1

        print(nums_count)
        sorted_nums_count = sorted(nums_count.items(), key=lambda item: item[1], reverse=True)
        print(sorted_nums_count)
        
        result = []
        for i in range(k):
            result.append(sorted_nums_count[i][0])

        return result