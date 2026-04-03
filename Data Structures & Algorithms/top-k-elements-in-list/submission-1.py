class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     nums_count = {}

    #     for num in nums:
    #         nums_count[num] = nums_count.get(num, 0) + 1

    #     print(nums_count)
    #     sorted_nums_count = sorted(nums_count.items(), key=lambda item: item[1], reverse=True)
    #     print(sorted_nums_count)
        
    #     result = []
    #     for i in range(k):
    #         result.append(sorted_nums_count[i][0])

    #     return result
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        print(count)
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if (len(result) == k):
                    return result